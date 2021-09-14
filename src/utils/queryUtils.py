def region_list_query():
    return "MATCH (w)-[grown:grown_in]->(r:Individual)-[:region_of*]->(sr) RETURN r.label, sr.label"


def varietal_list_query():
    return "MATCH (w)-[:SUBCLASSOF]->(x {label: 'varietal'}) RETURN DISTINCT w.label as label"


def wine_list_query():
    return "MATCH (w {label: 'wine'})<-[:SUBCLASSOF*]-(x) RETURN DISTINCT x.label as label"


def wine_query(region, colour, varietal):
    r = " WHERE r.label='%s' or subR.label='%s'" % (region, region) if region else ""
    c = " {label: '%s'}" % (colour) if colour else ""
    v = " {label: '%s'}" % (varietal) if varietal else ""
    return """
        MATCH (w {label: 'wine'})<-[:SUBCLASSOF*]-(x)-[:grown_in]->(r)-[:region_of*]->(subR)%s
        MATCH (w {label: 'wine'})<-[:SUBCLASSOF*]-(x)-[:has_color]->(c%s)
        MATCH (w {label: 'wine'})<-[:SUBCLASSOF*]-(x)-[:made_from]->(v%s)
        RETURN DISTINCT x.label as label""" % (r, c, v)


def get_result(driver, query):
    result = set()
    with driver.session() as session:
        r = session.run(query)
        for x in r.data():
            result.update(x.values())
    return list(result)
