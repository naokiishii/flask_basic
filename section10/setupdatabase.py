from basic import db, Puppy, app

with app.app_context():
  # CREATES ALL THE TABLES Model --> DB Table
  db.create_all()

  sam = Puppy('Sammy', 3)
  frank = Puppy('Frankie', 4)

  print(sam.id)
  print(frank.id)

  db.session.add_all([sam, frank])
  # db.session.add(sam)
  # db.session.add(frank)

  db.session.commit()

  print(sam.id)
  print(frank.id)