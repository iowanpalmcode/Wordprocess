from categories import climb, swim, run, fly, jump, crawl, hide, hunt, sleep, communicate

"""
    # Obs. pick = {
    "climbc": climb,
    "swimc": swim,
    "runc": run,
    "flyc": fly,
    "jumpc": jump,
    "crawlc": crawl,
    "hidec": hide,
    "huntc": hunt,
    "sleepc": sleep,
    "communicatec": communicate
}"""
# For ease, will just use 10 syn lists 
# 10 dicitonaries for similar words for all 10 words in categories. py
# Run, Swim, Climb, Fly, Jump, Crawl, Hide, Hunt, Sleep, Communicate

flysim = ["soar", "glide", "hover", "flit", "zoom", "drift", "swoop", "aviate", "sail", "wing", "fly"]
runsim = ["sprint", "dash", "gallop", "jog", "scamper", "bolt", "race", "hasten", "speed", "scurry", "run"]
swimsim = ["glide", "paddle", "stroke", "float", "dive", "submerge", "wade", "bodyboard", "breaststroke", "tread", "swim"]
climbsim = ["scale", "mount", "ascend", "clamber", "scrabble", "climb", "shirker", "soar", "reach", "escalate","surmount"]
jumpsim = ["leap", "bound", "hop", "skip", "vault", "spring", "pounce", "hitch", "bhop", "launch", "jump"]
crawlsim = ["crawl", "creep", "inch", "slither", "worm", "skulk", "grovel", "pad", "drag", "edge", "sneak"]
hidesim = ["hide", "conceal", "camouflage", "cover", "bury", "shroud", "obscure", "mask", "screen", "shelter", "cache"]
huntsim = ["hunt", "stalk", "track", "search", "pursue", "forage", "trail", "chase", "hound", "trawl", "seek"]
sleepsim = ["sleep", "doze", "slumber", "rest", "nap", "snooze", "hibernate", "repose", "drowse", "crash", "kip"]
communicatesim = ["communicate", "convey", "express", "transmit", "interact", "disclose", "correspond", "articulate", "share", "impart", "network"]
# 30/30/30/20
negators = [
    "no", "not", "none", "no one", "nobody", "nothing", "neither", "nor", "nowhere", 
    "never", "hardly", "barely", "scarcely", "seldom", "rarely", "little", "few", 
    "without", "against", "cannot", "can't", "could not", "couldn't", "do not", 
    "don't", "does not", "doesn't", "did not", "didn't", "will not", "won't", 
    "would not", "wouldn't", "shall not", "shan't", "should not", "shouldn't", 
    "may not", "might not", "must not", "mustn't", "is not", "isn't", "are not", 
    "aren't", "was not", "wasn't", "were not", "weren't", "has not", "hasn't", 
    "have not", "haven't", "had not", "hadn't", "cannot have", "need not", 
    "needn't", "dare not", "daren't", "lack", "lacking", "lacks", "lacked", 
    "fail", "failing", "fails", "failed", "refuse", "refusing", "refuses", 
    "refused", "reject", "rejecting", "rejects", "rejected", "deny", "denying", 
    "denies", "denied", "exclude", "excluding", "excludes", "excluded", "prevent", 
    "preventing", "prevents", "prevented", "prohibit", "prohibiting", "prohibits", 
    "prohibited", "ban", "banning", "bans", "banned", "avoid", "avoiding", 
    "avoids", "avoided"
]
