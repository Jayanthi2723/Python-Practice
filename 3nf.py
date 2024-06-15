def is_3nf(relation):
  """Returns True if the relation is in 3NF, False otherwise."""

  for attribute in relation.attributes:
    if attribute.is_foreign_key():
      if attribute.is_null_allowed():
        return False

  for attribute in relation.attributes:
    if attribute.is_primary_key() and attribute.is_foreign_key():
      if not attribute.is_unique():
        return False

  return True


def check_3nf(relations):
  """Checks if all the relations are in 3NF."""

  for relation in relations:
    if not is_3nf(relation):
      print("The relation {} is not in 3NF.".format(relation.name))


if __name__ == "__main__":
  relations = [
      Relation("Customers", ["CustomerID", "Name", "Address"]),
      Relation("Orders", ["OrderID", "CustomerID", "OrderDate", "Total"]),
  ]

  check_3nf(relations)
