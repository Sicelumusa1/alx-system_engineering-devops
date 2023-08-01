#!/usr/bin/env ruby
def school_match(string)
    match_found = string.scan(/hbt*n/)

    if match_found.any?
      puts match_found.join("\n")
    else
      puts ""
    end
end
school_match(ARGV[0])
