#!/usr/bin/perl

use strict;
use warnings;

my $num_args = $#ARGV + 1;

foreach my $argnum (0 .. $#ARGV)
{
    print "$ARGV[$argnum] \n";
    open(my $file_handle, '<:encoding(UTF-8)', $ARGV[$argnum])
        or die "Couldn't do it, chief";

    while(my $row = <$file_handle>)
    {
        chomp $row;
        print "$row\n";
    }
}

