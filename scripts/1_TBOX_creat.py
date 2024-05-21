from rdflib.namespace import RDFS, RDF, XSD
from rdflib import Graph, Namespace, Literal

# Create a Graph
graph = Graph()

URI = Namespace("http://SDM_lab_2.org/")

graph.bind('lab',URI)

############## （1) Class Paper ######################
graph.add((URI.ResearchPaper, RDF.type, RDFS.Class))
graph.add((URI.ResearchPaper, RDFS.label, Literal("ResearchPaper")))

# Property of Paper
graph.add((URI.Cites, RDF.type, RDF.Property))
graph.add((URI.Cites, RDFS.domain, URI.ResearchPaper))
graph.add((URI.Cites, RDFS.range, URI.ResearchPaper))
graph.add((URI.Cites, RDFS.label, Literal("Cites")))

graph.add((URI.Topics, RDF.type, RDFS.Class))
graph.add((URI.Topics, RDFS.label, Literal("Topics")))

graph.add((URI.HasTopics, RDF.type, RDF.Property))
graph.add((URI.HasTopics, RDFS.domain, URI.ResearchPaper))
graph.add((URI.HasTopics, RDFS.range, URI.Topics))
graph.add((URI.HasTopics, RDFS.label, Literal("HasTopics")))

graph.add((URI.SubmittedPaper, RDF.type, RDFS.Class))
graph.add((URI.SubmittedPaper, RDFS.label, Literal("SubmittedPaper")))

graph.add((URI.Submitted, RDF.type, RDF.Property))
graph.add((URI.Submitted, RDFS.domain, URI.ResearchPaper))
graph.add((URI.Submitted, RDFS.range, URI.SubmittedPaper))
graph.add((URI.Submitted, RDFS.label, Literal("Submitted")))

# Attributes of Paper 
# (1) PaperTitle
graph.add((URI.PaperTitle, RDF.type, RDF.Property))
graph.add((URI.PaperTitle, RDFS.domain, URI.ResearchPaper))
graph.add((URI.PaperTitle, RDFS.range, XSD.string))
graph.add((URI.PaperTitle, RDFS.label, Literal("PaperTitle")))

# (2) PaperAbstract
graph.add((URI.PaperAbstract, RDF.type, RDF.Property))
graph.add((URI.PaperAbstract, RDFS.domain, URI.ResearchPaper))
graph.add((URI.PaperAbstract, RDFS.range, XSD.string))
graph.add((URI.PaperAbstract, RDFS.label, Literal("PaperAbstract")))

############## （2) Class Person ######################
graph.add((URI.Person, RDF.type, RDFS.Class))
graph.add((URI.Person, RDFS.label, Literal("Person")))

# Subclasses of Person
# (2.1) Author
graph.add((URI.Author, RDF.type, RDFS.Class))
graph.add((URI.Author, RDFS.subClassOf, URI.Person))
graph.add((URI.Author, RDFS.label, Literal("Author")))

# Attributes of Author 
# graph.add((URI.AuthorName, RDF.type, RDF.Property))
# graph.add((URI.AuthorName, RDFS.domain, URI.Author))
# graph.add((URI.AuthorName, RDFS.range, XSD.string))
# graph.add((URI.AuthorName, RDFS.label, Literal("AuthorName")))

graph.add((URI.Write, RDF.type, RDF.Property))
graph.add((URI.Write, RDFS.domain, URI.Author))
graph.add((URI.Write, RDFS.range, URI.ResearchPaper))
graph.add((URI.Write, RDFS.label, Literal("Write")))

# graph.add((URI.CorrespondingAuthor, RDF.type, RDF.Property))
# graph.add((URI.CorrespondingAuthor, RDFS.subPropertyOf, URI.Write))
# graph.add((URI.CorrespondingAuthor, RDFS.domain, URI.Author))
# graph.add((URI.CorrespondingAuthor, RDFS.range, URI.ResearchPaper))
# graph.add((URI.CorrespondingAuthor, RDFS.label, Literal("CorrespondingAuthor")))

# (2.2) Reviewer
graph.add((URI.Reviewer, RDF.type, RDFS.Class))
graph.add((URI.Reviewer, RDFS.subClassOf, URI.Person))
graph.add((URI.Reviewer, RDFS.label, Literal("Reviewer")))

graph.add((URI.WriteReview, RDF.type, RDF.Property))
graph.add((URI.WriteReview, RDFS.domain, URI.Reviewer))
graph.add((URI.WriteReview, RDFS.range, URI.SubmittedPaper))
graph.add((URI.WriteReview, RDFS.label, Literal("WriteReview")))

graph.add((URI.ReviewText, RDF.type, RDFS.Class))
graph.add((URI.ReviewText, RDFS.label, Literal("ReviewText")))

graph.add((URI.ReviewOf, RDF.type, RDF.Property))
graph.add((URI.ReviewOf, RDFS.domain, URI.ReviewText))
graph.add((URI.ReviewOf, RDFS.range, URI.SubmittedPaper))
graph.add((URI.ReviewOf, RDFS.label, Literal("ReviewOf")))

# graph.add((URI.AcceptPossibility, RDF.type, RDF.Property))
# graph.add((URI.AcceptPossibility, RDFS.domain, URI.ReviewText))
# graph.add((URI.AcceptPossibility, RDFS.range, XSD.int))
# graph.add((URI.AcceptPossibility, RDFS.label, Literal("AcceptPossibility")))

############## （3) Class Journal ######################
graph.add((URI.Journal, RDF.type, RDFS.Class))
graph.add((URI.Journal, RDFS.label, Literal("Journal")))

graph.add((URI.Volumes, RDF.type, RDFS.Class))
graph.add((URI.Volumes, RDFS.label, Literal("Volumes")))

# Adding attribute for volume
# graph.add((URI.VolumeYear, RDF.type, RDF.Property))
# graph.add((URI.VolumeYear, RDFS.domain, URI.Volume))
# graph.add((URI.VolumeYear, RDFS.range, XSD.int))
# graph.add((URI.VolumeYear, RDFS.label, Literal("VolumeYear")))

# Adding properties for journal
# Attribute of Journal
# graph.add((URI.JournalTitle, RDF.type, RDF.Property))
# graph.add((URI.JournalTitle, RDFS.domain, URI.Journal))
# graph.add((URI.JournalTitle, RDFS.range, XSD.string))
# graph.add((URI.JournalTitle, RDFS.label, Literal("JournalTitle")))

graph.add((URI.OfJournal, RDF.type, RDF.Property))
graph.add((URI.OfJournal, RDFS.domain, URI.Journal))
graph.add((URI.OfJournal, RDFS.range, URI.Volumes))
graph.add((URI.OfJournal, RDFS.label, Literal("OfJournal")))

# Proceedings 
graph.add((URI.Proceedings, RDF.type, RDFS.Class))
graph.add((URI.Proceedings, RDFS.label, Literal("Proceedings")))

### Venue added
graph.add((URI.Venue, RDF.type, RDFS.Class))
graph.add((URI.Venue, RDFS.label, Literal("Venue")))

graph.add((URI.InVenue, RDF.type, RDF.Property))
graph.add((URI.InVenue, RDFS.domain, URI.Proceedings))
graph.add((URI.InVenue, RDFS.range, URI.Venue))
graph.add((URI.InVenue, RDFS.label, Literal("InVenue")))

graph.add((URI.Conference, RDF.type, RDFS.Class))
graph.add((URI.Conference, RDFS.label, Literal("Conference")))

# Adding attribute for conference
# graph.add((URI.ConferenceTitle, RDF.type, RDF.Property))
# graph.add((URI.ConferenceTitle, RDFS.domain, URI.Conference))
# graph.add((URI.ConferenceTitle, RDFS.range, XSD.string))
# graph.add((URI.ConferenceTitle, RDFS.label, Literal("ConferenceTitle")))

# Property of Conference
graph.add((URI.BelongTo, RDF.type, RDF.Property))
graph.add((URI.BelongTo, RDFS.domain, URI.Conference))
graph.add((URI.BelongTo, RDFS.range, URI.Proceedings))
graph.add((URI.BelongTo, RDFS.label, Literal("BelongTo")))

# SubClasses of Conference
# (1) Workshop
graph.add((URI.Workshop, RDF.type, RDFS.Class))
graph.add((URI.Workshop, RDFS.subClassOf, URI.Conference))
graph.add((URI.Workshop, RDFS.label, Literal("Workshop")))

# (2)) RegularConference
graph.add((URI.RegularConference, RDF.type, RDFS.Class))
graph.add((URI.RegularConference, RDFS.subClassOf, URI.Conference))
graph.add((URI.RegularConference, RDFS.label, Literal("RegularConference")))

# Properties of proceeding
graph.add((URI.WorkshopIn, RDF.type, RDF.Property))
graph.add((URI.WorkshopIn, RDFS.domain, URI.Workshop))
graph.add((URI.WorkshopIn, RDFS.range, URI.Proceedings))
graph.add((URI.WorkshopIn, RDFS.label, Literal("WorkshopIn")))

graph.add((URI.ConIn, RDF.type, RDF.Property))
graph.add((URI.ConIn, RDFS.domain, URI.RegularConference))
graph.add((URI.ConIn, RDFS.range, URI.Proceedings))
graph.add((URI.ConIn, RDFS.label, Literal("ConIn")))

# Adding attributes for proceedings
# graph.add((URI.ProceedingName, RDF.type, RDF.Property))
# graph.add((URI.ProceedingName, RDFS.domain, URI.Proceedings))
# graph.add((URI.ProceedingName, RDFS.range, XSD.string))
# graph.add((URI.ProceedingName, RDFS.label, Literal("ProceedingName")))	

# graph.add((URI.ProceedingYear, RDF.type, RDF.Property))
# graph.add((URI.ProceedingYear, RDFS.domain, URI.Proceedings))
# graph.add((URI.ProceedingYear, RDFS.range, XSD.int))
# graph.add((URI.ProceedingYear, RDFS.label, Literal("ProceedingYear")))


graph.add((URI.IsInProceeding, RDF.type, RDF.Property))
graph.add((URI.IsInProceeding, RDFS.domain, URI.ResearchPaper))
graph.add((URI.IsInProceeding, RDFS.range, URI.Proceedings))
graph.add((URI.IsInProceeding, RDFS.label, Literal("IsInProceeding")))

graph.add((URI.IsInJournal, RDF.type, RDF.Property))
graph.add((URI.IsInJournal, RDFS.domain, URI.ResearchPaper))
graph.add((URI.IsInJournal, RDFS.range, URI.Volumes))
graph.add((URI.IsInJournal, RDFS.label, Literal("IsInJournal")))

# Print out the entire Graph in the RDF Turtle format
print(graph.serialize('data/lab_tbox.ttl',format="ttl"))

