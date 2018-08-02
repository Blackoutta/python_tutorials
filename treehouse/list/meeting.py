attendees = ["Ken", "Alena", "Treasure"]
#Append
attendees.append("Ashley")
#Extend
attendees.extend(["James", "Guil"])
optional_invitees = ["Ben J.", "Dave"]
potential_attendees = attendees + optional_invitees
print("There are",len(potential_attendees), "potential attendees currently")

#Join
to_line = ",".join(attendees)
cc_line = ",".join(optional_invitees)
print("To:  " + to_line)
print("Cc:  " + cc_line)
