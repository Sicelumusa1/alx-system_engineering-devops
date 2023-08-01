#!/usr/bin/env ruby
def school_match(string)
    patten = /hbt*n/

    match_found = string.match(patten)

    if match_found
      puts match_found[0]
    else
      puts ""
    end
end

input = ARGV[0]

school_match(input)
