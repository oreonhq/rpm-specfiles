#!/usr/bin/perl

#############################################################################
#
# kpcli - KeePass Command Line Interface
#
# Author: Lester Hightower <hightowe at cpan dot org>
#
# This program was inspired by "kedpm -c" and resulted despite illness
# (or more likely because of it) over the USA Thanksgiving holiday in
# late November of 2010. As a long-time user of the Ked Password Manager
# I really missed a command line interface after getting an Android cell
# phone and switching to KeePass, so that I could access my password
# database on my phone. This program scratches that itch.
#
# Reference information on the KeePass file format:
# https://gist.github.com/lgg/e6ccc6e212d18dd2ecd8a8c116fb1e45
#
#############################################################################

#############################################################################
# ===========================================================================
# Overview of UTF-8 support
# ===========================================================================
# With v4.1, substantial utf8 support was added in reponse to SF bug #53.
# The support almost certainly is not perfect, but things have surely lept
# ahead of where they were. The large (and possibly breaking) changes that
# v4.1 introduces are the assumptions that all strings in KDBX files are to
# be stored as utf8 and that terimals running kpcli can support utf8. In the
# year 2024, these seem like reasonable assumptions, but I do worry a bit
# that kpcli may be in use on some very limited, remote-only systems. If
# someone is bitten by the new utf8 support in v4.1 that, --noutf8 does not
# correct, please open a bug report explaing your situation.
#
# Some basic and important context
# --------------------------------
# 1. File::KeePass does not handle Unicode (utf8) characters correctly.
# 2. File::KDBX was built with the assumption that all strings are utf8.
# 3. For File::KDBX, strings should be passed and are returned as utf8 text.
# 4. When reading and writing databases, File::KDBX encodes and decodes text
#    correctly to insure database file compatibility with other applications.
# 5. Term::ShellUI does not seem to be able to accept utf8 strings for tab
#    completion options. Term::ReadLine::Gnu seems to show the non-utf8
#    strings correctly, most likely coincidentally based on LANG=*.UTF-8,
#    but giving utf8 strings as tab completion options breaks Term::ShellUI.
# 6. Due to Term::ShellUI's utf8 issue, these state variables are built and
#    stored non-utf8, by build_all_group_paths()/build_all_entry_paths():
#      - all_grp_paths_fwd, all_grp_paths_rev
#      - all_ent_paths_fwd, all_ent_paths_rev
# 7. That means that any access into those state variables must be via
#    non-utf8 strings. Access is almost always accomplished by first calling
#    normalize_path_string() and so it cannnot deal in utf8 strings. Well,
#    technically it could perhaps be modified to do so, but I think it is
#    best to have it complain and not introduce code that gives it utf8.
# 8. The password fields are intentionally not utf8 encoded which follows
#    what File::KDBX does and I assume other programs as well.
#
#############################################################################


###########################################################################
# I chose to place a few modules above the BEGIN block because these didn't
# seem to have a negative impact, and I use Data::Dumper in the BEGIN block
# for debugging.
###########################################################################
use 5.9.4;   # Version when Module::Loaded was added
use strict;                     # core
use diagnostics;                # core
use version;                    # core
no utf8;                        # Never treat strings in source code as utf8
use Encode qw();                # core - do not want any functions imported
use Data::Dumper qw(Dumper);    # core
$Data::Dumper::Sortkeys = 1; # Sort hash keys
$Data::Dumper::Useqq = 1;    # Escape non-printable characters
$Data::Dumper::Useperl = 1;  # Use the pure-perl implementation
# Overriding *Data::Dumper::qquote as shown just below will have Dumper()
# print *actual* UTF-8 characters instead of escaping them. This is not
# very useful in practical development, but I want to keep it around.
# https://stackoverflow.com/questions/50489062/how-to-display-readable-utf-8-strings-with-datadumper
if (0) { # Print unprintable characters
  no warnings 'redefine';
  *Data::Dumper::qquote = sub { qq["${\(shift)}"] };
}

###########################################################################
# This BEGIN code is used to unshift local perl module paths (~/perl5/*)
# onto @INC to allow users to install modules for kpcli into thier homedirs
# instead of having to do it at the system level. This is convenient with
# cpanm and can be helpful on hosts without root privilege.
###########################################################################
BEGIN {
  # Bail immediately if we're on Windows
  if (lc($^O) =~ m/^mswin/) { return 0; }

  # NOTE: Stopped using File::Find in here because doing so pulled
  # in other modules that the user may prefer to load from ~/perl5.
  # This was specifically a problem for List::Util when support was
  # added to cli_pwck() for XData::Password::zxcvbn on perl v5.22.1.
  sub get_dirs {
    my $dir = shift @_;
    if (! -d $dir) { return (); } # Nothing to do if $dir is not a dir
    # Push all subdirs of $dir onto @d
    my @d = ();
    opendir(my $dh, $dir) || return ();
    while ($_ = readdir($dh)) {
      next if $_ eq "." or $_ eq "..";
      my $fn = $dir . '/' . $_;
      if (-d $fn) { push @d, $fn; }
    }
    closedir($dh);
    # Look for directories in each subdirectory of $dir
    my @d2=(); foreach (@d) { push @d2, get_dirs($_); }
    return ($dir, @d2); # Return $dir and its subdirs
  }

  # cPanelUserConfig.pm was the reference code from which I
  # built this, but I modified it substantially, to the
  # point that it is really not the same any longer and, I
  # believe, should work on many more unix-like systems.
  # I also added checks so that we don't push non-existant
  # directories onto @INC.
  # NOTE: An alternative to this may be CPAN module local::lib,
  # but it would bring in many more dependancies...

  # $b__dir will be something like /home/<user>/perl5
  my $b__dir = ( getpwuid($>) )[7] . '/perl5';
  if (! -d $b__dir) { return 0; } # Nothing to do if no ~/perl5/

  # Find all of .../auto/ directories in ~/perl5, chop the /auto off,
  # and append that list of directories to @add_paths.
  my @subdirs = get_dirs($b__dir);
  my @auto_dirs = map { $_ =~ s%/auto$%%; $_; } grep(m%/auto$%, @subdirs);
  #warn "LHHD: \@auto_dirs:\n" . join("\n", @auto_dirs) . "\n\n";

  # Potential base set of ~/perl5 paths to be placed into @INC
  my @add_paths = ( $b__dir.'/lib/perl5', @auto_dirs );

  # Potential complete set of ~/perl5 paths to be placed into @INC
  my @INC_adds = ();
  unshift @INC_adds, @add_paths, map { $b__dir . $_ } grep {$_ ne '.'} @INC;

  # Any @INC_adds that exist will go into @INC_toadd to be unshifted to @INC
  my @INC_toadd = ();
  foreach my $inc_add (@INC_adds) {
    next if (grep(/^\Q$inc_add\E$/, @INC)); # Don't add if already there
    if (-d $inc_add) { push @INC_toadd, $inc_add; }
  }

  #warn "LHHD: \@INC_adds:\n" . join("\n", @INC_adds) . "\n\n";
  #warn "LHHD: \@INC_toadd:\n" . join("\n", @INC_toadd) . "\n\n";
  unshift @INC, @INC_toadd;
  #warn "LHHD: \@INC:\n" . join("\n", @INC) . "\n\n";
}

########################
# The required modules #
########################
# Required core modules
use Cwd qw(abs_path);                         # core
use File::Copy qw(move);                      # core
use File::Spec;                               # core
use FileHandle;                               # core
use Getopt::Long;                             # core
use File::Basename;                           # core
use Digest::file;                             # core
use Digest::MD5;                              # core
use Digest::SHA qw(sha256);                   # core
use Term::ANSIColor;                          # core
use Carp qw(longmess);                        # core
use English qw(-no_match_vars);               # core
use Time::HiRes qw(gettimeofday tv_interval); # core
use Time::Local qw(timegm);                   # core
use Clone qw(clone);                          # core
use Time::Piece;                              # core
use Time::Seconds;                            # core
use Module::Loaded qw(is_loaded);             # core
use POSIX;                   # core, required for unsafe signal handling
Getopt::Long::Configure(qw(no_auto_abbrev));

# Required non-core modules
use Crypt::Rijndael;         # non-core, libcrypt-rijndael-perl on Ubuntu
use Sort::Naturally;         # non-core, libsort-naturally-perl on Ubuntu
use Term::ReadKey;           # non-core, libterm-readkey-perl on Ubuntu
use Term::ShellUI;           # non-core, libterm-shellui-perl on Ubuntu
use File::KeePass 0.03;      # non-core, libfile-keepass-perl on Ubuntu
                             #  - >=v0.03 needed due critical bug fixes
##############################
# End of required modules ####
##############################

my $DO_TRACE_DUMPS = 0; # Do trace dumps or not? Usually on for development.
my $DUMP_PATHS_ON_OPEN_AND_MKTESTDB = 0; # Just for dev/debugging

# A developer convenience to force using a particular Term::ReadLine module
our $FORCED_READLINE = undef;	# Auto-select
#our $FORCED_READLINE = 'Term::ReadLine::Gnu';
#our $FORCED_READLINE = 'Term::ReadLine::Perl';
#our $FORCED_READLINE = 'Term::ReadLine::Perl5';

# Pull in optional perl modules with run-time loading
my %OPTIONAL_PM=();

# File::KDBX holds a special place: "Recommended" but truly optional.
my $MIN_FILE_KDBX_VER = '0.906';
runtime_load_module({},'File::KDBX',undef);
if (is_loaded('File::KDBX')) {
  runtime_load_module(\%OPTIONAL_PM,'File::KDBX::Constants',[ qw(:all) ]);
  runtime_load_module(\%OPTIONAL_PM,'File::KDBX::Key',[ qw() ]);
  my @errs = can_kdbx();
  if (scalar(@errs)) {
    print color('bold yellow') .
	"WARNING: " .
	color('clear') . color('red') .
	"There are problems with File::KDBX, as follows:\n".
	" - ".join("\n - ", @errs)."\n".
	color('clear');
  }
}

# If DO_TRACE_DUMPS is true we'll need Devel::StackTrace
# libdevel-stacktrace-perl or perl-Devel-StackTrace.noarch
if ($DO_TRACE_DUMPS) {
  if (! runtime_load_module(\%OPTIONAL_PM,'Devel::StackTrace', undef)) {
    warn color('yellow') .
	"Failed to load Devel::StackTrace. Setting DO_TRACE_DUMPS=0..." .
	color('clear') . "\n";
    $DO_TRACE_DUMPS = 0;
  }
}

# Capture::Tiny is needed to safely optionally-load Clipboard.
# Clipboard is needed by the clipboard copy commands (xw, xu, xp, and xx).
if (runtime_load_module(\%OPTIONAL_PM,'Capture::Tiny',[qw(capture)])) {
  # Clipboard tests its dependencies at import() and writes warnings to STDERR.
  # Capture::Tiny is used to catch those warnings and we silently hold them
  # until and unless someone tries to use dependant functions.
  my ($out, $err, @result) = capture(
		sub { runtime_load_module(\%OPTIONAL_PM,'Clipboard',undef); } );
  if (length($err)) {
    # Cleanup the error message for for better viewing by the user
    $err =~ s/^\s+//g; $err =~ s/\s+$//g; $err =~ s/^(.*)$/ > $1/mg;
    $OPTIONAL_PM{'Clipboard'}->{error} = $err;
  }
} else {
  # If we didn't get Capture::Tiny, also mark Clipboard as not loaded.
  $OPTIONAL_PM{'Clipboard'}->{loaded} = 0;
}
# Optional but helpful modules for Windows
if (lc($OSNAME) =~ m/^mswin/) {
  # Win32::Console::ANSI is needed to emulate ANSI colors on Windows
  if (! runtime_load_module(\%OPTIONAL_PM,'Win32::Console::ANSI',undef)) {
    # If we don't have Win32::Console::ANSI then we want to override
    # &main::color() and colored() from Term::ANSIColor with NOOPs.
    no strict 'refs';
    *color = sub { my $color = shift @_; return ''; };
    *colored = sub { my $color = shift @_; my $text=shift @_; return $text; };
  }
  # In version 3.5, added the use of Term::Size::Win32 to deal with a
  # problem when importing Term::ReadLine::Perl where it warns about
  # "The Win32 GetConsoleScreenBufferInfo call didn't work."
  if (! runtime_load_module(\%OPTIONAL_PM,'Term::Size::Win32',undef)) {
    # TODO - should we do something here...?
  }
}
runtime_load_module(\%OPTIONAL_PM,'Sub::Install',undef);
# Optionally use a more cryptographically secure RNG.
our $RNG_EXT = undef;
if (runtime_load_module(\%OPTIONAL_PM,'Math::Random::ISAAC',undef)) {
  $RNG_EXT = Math::Random::ISAAC->new(
	int(1000000000 * (Time::HiRes::time() - int(Time::HiRes::time()))));
}
use subs 'rand'; # Override built-in rand() with our own function
sub rand {
  my $ceiling = shift @_ || 1;
  our $RNG_EXT;
  if (defined($RNG_EXT) && ref($RNG_EXT) eq 'Math::Random::ISAAC') {
    my $random = $RNG_EXT->rand() * $ceiling;
    return $random;
  }
  return CORE::rand($ceiling);
}
if (runtime_load_module(\%OPTIONAL_PM,'Authen::OATH',undef)) {
  runtime_load_module(\%OPTIONAL_PM,'Convert::Base32',[qw(decode_base32)]);
}
runtime_load_module(\%OPTIONAL_PM,'URI',undef);

$|=1; # flush immediately after writes or prints to STDOUT

my $DEBUG=0;
$Data::Dumper::Useqq = 1;    # Have Dumper escape special chars (like \0)
our $DEFAULT_PASSWD_LEN = 20;# Default length of generated passwords.
our $DEFAULT_PASSWD_MIN = 1; # Minimum length of generated passwords.
our $DEFAULT_PASSWD_MAX = 50;# Maximum length of generated passwords.
my $DEFAULT_ENTRY_ICON = 0;  # In keepassx, icon 0 is a golden key
my $DEFAULT_GROUP_ICON = 49; # In keepassx, icon 49 is an opened file folder
my $DEFAULT_BAKUP_ICON = 43; # 43 = trash can in keepassx and KeePassXC
my $FOUND_DIR = '_found';    # The find command's results go in /_found/
my @ALL_FIND_FIELDS = qw(title username comment url tags);
my $AUTOSAVES_DIR = '_autosaves'; # The place where auto-saves are kept
my $MAX_ATTACH_SIZE = 2*1024**2;  # Maximum size of entry file attachments
my $KPXC_MIN_VER = '2.7.1';
# I like the U+21db character, but readline chokes on it and
# breaks tab completion... :(
#my $DUP_ENTRIES_FORMAT = " ⇶%02x"; # Rightwards Triple Arrow - U+21db
my $DUP_ENTRIES_FORMAT = " =>%02x";

# Application name and version
my $APP_NAME = basename($0);  $APP_NAME =~ s/\.(pl|exe)$//;
my $VERSION = "4.1.3";

our $HISTORY_FILE = ""; # Gets set in the MyGetOpts() function
our $PASSWD_ECHO_CHAR = '*';
our $opts = MyGetOpts(); # Will only return with options we think we can use

our $NO_UTF8 = $opts->{noutf8}; # Disables utf8 support if --noutf8 is given
# This variable controls if all user input is converted into utf8 format.
# It needs to be respected in all placed that take user input and, luckily,
# most of those call get_prepped_readline_term(). That known inventory is:
#  - new_edit_single_line_input()
#  - new_edit_multiline_input()
#  - edit_entry_strings()
#  - prompt_filename_from_user()
#  - cli_rename()
#  - cli_icons() ** not an issue because it only takes numbers
# Other impacted functions:
#  - cli_mktestdb() for pretty obvious reasons... :)
#  - cli_new() because the title can be given with the command
#  - cli_set() because the key/val pair is given with the command
#  - cli_copy() because the title is given with the command
#  - cli_rename()
# This variable mostly blocks calls to decode_if_not_utf8().
our $ALL_USER_INPUT_TO_UTF8 = 1;
# On 04/15/2024, after a few days of learning and testing, I decided to
# default to KDB1_STRS_TO_UTF8=1 as that seems to be most interoperable
# with KeePassX. This default can be overridden by both --noutf8 and by
# the "utf8 off" command.
our $KDB1_STRS_TO_UTF8 = 1; # Decode File::KeePass KDBv1 strings to UTF-8?
set_stdio_binmode(); # Set the STDIO binmode

my $doc_passwd_gen =
	"For password generation, the \"g\" method produces a\n" .
	"string of random characters, the \"w\" method creates a\n" .
	"4-word string inspired by \"correct horse battery staple\"\n" .
	"(http://xkcd.com/936/), and the \"i\" method provides an\n" .
	"interactive user interface to the \"g\" and \"w\" methods.\n" .
	"\n" .
	"By default, the \"g\" and \"i\" methods generate passwords that\n" .
	"are $DEFAULT_PASSWD_LEN characters long. " .
				"That can be controlled by providing an\n" .
	"integer immediately after the \"g|i\" in the range of "
				. "$DEFAULT_PASSWD_MIN-$DEFAULT_PASSWD_MAX.\n" .
	"For example, \"g17\" will generate a 17 character password.\n" .
	"";
# Setup our Term::ShellUI object
my $term = new Term::ShellUI(
    app => $APP_NAME,
    term => get_readline_term(\%OPTIONAL_PM, $APP_NAME),
    history_file => $HISTORY_FILE,
    keep_quotes => 0,
    commands => {
         "autosave" => {
             desc => "Autosave functionality",
             doc => "\n" . cli_autosave(undef,undef,1),
             method => \&cli_autosave,
             minargs => 0, maxargs => 1,
             timeout_exempt => 1,
         },
         "ver" => {
             desc => "Print the version of this program",
             doc => "\n" .
		"Add the -v option to get an inventory of the versions\n" .
		"of the various dependencies being used. Please provide\n" .
		"that information in any bug reports filed.\n" .
		"",
             method => \&cli_version,
             minargs => 0, maxargs => 1,
	     exclude_from_history => 1,
             timeout_exempt => 1,
         },
         "version" => { alias => "ver",
             exclude_from_completion=>1, exclude_from_history => 1,
             timeout_exempt => 1,
         },
         "vers" => {
             desc => "Same as \"ver -v\"",
             minargs => 0, maxargs => 1,
             method => \&cli_versions,
             exclude_from_completion=>1, exclude_from_history => 1,
             timeout_exempt => 1,
         },
         "versions" => { alias => "vers",
             exclude_from_completion=>1, exclude_from_history => 1,
             timeout_exempt => 1,
         },
         "help" => {
             desc => "Print helpful information",
             args => sub { shift->help_args(undef, @_); },
             method => sub { my_help_call(@_); },
	     exclude_from_history => 1,
             timeout_exempt => 1,
             #method => sub { shift->help_call(undef, @_); }
         },
         "h" => { alias => "help",
             exclude_from_completion=>1, exclude_from_history => 1,
             timeout_exempt => 1,
		},
         "?" => { alias => "help",
             exclude_from_completion=>1, exclude_from_history => 1,
             timeout_exempt => 1,
		},
	 "cls" => {
	     desc => 'Clear screen ("clear" command also works)',
	     doc  => "\n" .
		"Clear the screen, which is useful when guests arrive.\n",
	     maxargs => 0,
	     method => \&cli_cls,
	     exclude_from_history => 1,
             timeout_exempt => 1,
	 },
         "clear" => { alias => "cls", exclude_from_history => 1,
						timeout_exempt => 1, },
         "quit" => {
             desc => "Quit this program (EOF and exit also work)",
             maxargs => 0,
             method => sub { run_no_TSTP(\&cli_quit, @_); },
	     exclude_from_history => 1,
             timeout_exempt => 1,
         },
         "exit" => { alias => "quit", exclude_from_history => 1,
						timeout_exempt => 1, },
         # Generally, commands above here are timeout_exempt
         #"" => { args => sub { shift->complete_history(@_) } },
         "history" => { desc => "Prints the command history",
            doc => "\nSpecify a number to list the last N lines of history.\n" .
            "Pass -c to clear the command history.\n" .
            "Pass -d NUM to delete a single item.\n",
            args => "[-c] [-d] [number]",
            method => sub { shift->history_call(@_) },
	    exclude_from_history => 1,
         },
         "cd" => {
             desc => "Change directory (path to a group)",
             doc => "\n" .
		"Change the pwd to an absolute or relative path.\n" .
		"Slashes in names are escaped with backslashes:\n" .
		"(i.e. \"cd /personal/Comcast\\/Xfinity\").\n",
             maxargs => 1,
             args => \&complete_groups,
             method => \&cli_cd,
         },
         "chdir" => { alias => 'cd' },
         "cl" => {
             desc => "Change directory and list entries (cd+ls)",
             doc => "\n" .
		"Change the pwd to an absolute or relative path\n" .
		"and list the entries there. This is a useful way\n" .
		"to quickly navigate to a path and have the entries\n" .
		"listed in preparation to run the show command.\n",
             maxargs => 1,
             args => \&complete_groups,
             method => sub { if(cli_cd(@_) == 0) { cli_ls() } },
         },
         "saveas" => {
             desc => "Save to a specific filename " .
				"(saveas <file.kdb> [<file.key>])",
             minargs => 1, maxargs => 2,
             args => [\&my_complete_onlyfiles, \&my_complete_onlyfiles],
             proc => sub { run_no_TSTP(\&cli_saveas, @_); },
         },
         "export" => {
             desc => "Export entries to a new KeePass DB " .
				"(export <file.kdb> [<file.key>])",
             doc => "\n" .
		"Use this command to export the full tree of groups\n" .
		"and entries to another KeePass database file on disk,\n" .
		"starting at your current path (pwd).\n" .
		"\n" .
		"This is a safer way to change your database password or\n" .
		"to move between v1 (*.kdb) and v2 (*.kdbx) file formats.\n" .
		"Export from /, verify that the new file is good, and then\n" .
		"remove your original file.\n",
             minargs => 1, maxargs => 2,
             args => [\&my_complete_onlyfiles, \&my_complete_onlyfiles],
             proc => sub { run_no_TSTP(\&cli_export, @_); },
         },
         "import" => {
             desc => "Import a password database " .
				"(import <file> <path> [<file.key>])",
             doc => "\n" .
		"Use this command to import an entire password DB\n" .
		"specified by <file> into a new group at <path>.\n" .
		"Supported file types are KeePass v1 and v2, and\n" .
		"Password Safe v3 (https://pwsafe.org/).\n",
             minargs => 2, maxargs => 3,
             args => [\&my_complete_onlyfiles,,\&complete_groups,
					\&my_complete_onlyfiles],
             proc => sub { run_no_TSTP(\&cli_import, @_); },
         },
         "reroot" => {
             desc => "Change the root group of a KDBX4 database",
             doc => "\n" .
		"Unlike KDBv1 and KDBX3 formats, KDBX4 databases\n" .
		"have exactly one root group. This command allows\n" .
		"you to make a different group the root group, and\n" .
		"thusly throw away all data that is not underneath\n" .
		"that group.\n" .
		"\n" .
		"In general, this command is not very useful, but it\n" .
		"may be if you are importing another database and,\n" .
		"after doing so, want to make one of its groups the\n" .
		"new root of the entire database.\n",
             maxargs => 1,
             args => \&complete_groups,
             method => sub { run_no_TSTP(\&cli_reroot, @_); },
         },
         "open" => {
             desc => "Open a KeePass database file " .
				"(open <file.kdb> [<file.key>])",
             minargs => 1, maxargs => 2,
             args => [\&my_complete_onlyfiles, \&my_complete_onlyfiles],
             proc => sub { run_no_TSTP(\&cli_open, @_); },
         },
         "newdb" => {
             desc => "Create a new, empty KeePass database.",
             minargs => 0, maxargs => 0,
             proc => sub { run_no_TSTP(\&cli_newdb, @_); },
         },
         "mktestdb" => {
             desc => "Make a new, pre-populated KeePass database for testing.",
             minargs => 0, maxargs => 0,
             proc => sub { run_no_TSTP(\&cli_mktestdb, @_); },
         },
         "mkdir" => {
             desc => "Create a new group (mkdir <group_name>)",
             minargs => 1, maxargs => 1,
             args => \&complete_groups,
             method => \&cli_mkdir,
         },
         "rmdir" => {
             desc => "Delete a group (rmdir <group_name>)",
             minargs => 1, maxargs => 1,
             args => \&complete_groups,
             method => \&cli_rmdir,
         },
         "dir" => { alias => "ls", },
         "ls" => {
             desc => "Lists items in the pwd or specified paths " .
							"(\"dir\" also works)",
             minargs => 0, maxargs => 99,
             args => \&complete_groups_and_entries,
             method => \&cli_ls,
         },
         "new" => {
             desc => "Create a new entry: new <optional path&|title>",
             doc => "\n" .
		"The new command is used to create a new entry.\n" .
		"\n" .
		"Usage is straightforward.\n" .
		"\n" .
		$doc_passwd_gen .
		"",
             minargs => 0, maxargs => 1,
             args => [\&complete_groups],
             method => sub { run_no_TSTP(\&cli_new, @_); },
         },
         "rm" => {
             desc => "Remove an entry: rm <path to entry|entry number>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => \&cli_rm,
         },
         "xu" => {
             desc => "Copy username to clipboard: xu <entry path|number>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { cli_xN('xu', @_); }
         },
         "xw" => {
             desc => "Copy URL (www) to clipboard: xw <entry path|number>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { cli_xN('xw', @_); }
         },
         "xp" => {
             desc => "Copy password to clipboard: xp <entry path|number>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { cli_xN('xp', @_); }
         },
         "xo" => {
             desc => "Copy one-time password to clipboard: xo <entry path|number>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { cli_xN('xo', @_); }
         },
         "xpx" => {
             desc => "Copy password to clipboard, with auto-clear: xpx <entry path|number>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { cli_xN('xpx', @_); }
         },
         "xx" => {
             desc => "Clear the clipboard: xx",
             minargs => 0, maxargs => 0,
             method => sub { cli_xN('xx'); }
         },
         "pwck" => {
             desc => "Check password quality: pwck <entry|group>",
             doc => "\n" .
		"The pwck command test password quality for entries.\n" .
		"You can check an individual entry or all entries inside\n" .
		"of a group, recursively. To check every password in your\n" .
		"database, use: pwck /\n" .
		"",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => \&cli_pwck,
         },
         "stats" => {
             desc => "Prints statistics about the open KeePass file",
             method => \&cli_stats,
         },
         "set" => {
             desc => "Set a value: get <entry path|entry number> <field> <val>",
             doc => "\n" .
		"The set command can take a path to an entry or an entry\n".
		"number (from the ls command), as its first argument,\n".
		"the field to change as its second argument, and that\n".
		"field's new value as the third argument.\n".
		"\n" .
		"When using entry numbers, they will refer to the last\n" .
		"path when an ls was performed or pwd if ls has not\n" .
		"yet been run.\n" .
		"",
             minargs => 3, maxargs => 3,
             args => [ \&complete_groups_and_entries,
			\&complete_get_set_fields ],
             method => \&cli_set,
         },
         "get" => {
             desc => "Get a value: get <entry path|entry number> <field>",
             doc => "\n" .
		"The get command can take a path to an entry or an entry\n".
		"number (from the ls command), as its first argument\n".
		"and the field to display as its second argument.\n".
		"\n" .
		"When using entry numbers, they will refer to the last\n" .
		"path when an ls was performed or pwd if ls has not\n" .
		"yet been run.\n" .
		"",
             minargs => 2, maxargs => 2,
             args => [ \&complete_groups_and_entries,
			\&complete_get_set_fields ],
             method => \&cli_get,
         },
         "show" => {
             desc => "Show an entry: show [-f] [-a] <entry path|entry number>",
             doc => "\n" .
		"The show command tries to intelligently determine\n" .
		"what you want to see and to make it easy to display.\n" .
		"Show can take a path to an entry as its argument or\n" .
		"an entry number as shown by the ls command.\n" .
		"\n" .
		"When using entry numbers, they will refer to the last\n" .
		"path when an ls was performed or pwd if ls has not\n" .
		"yet been run.\n" .
		"\n" .
		"By default, passwords are \"hidden\" by being displayed as\n" .
		"\"red on red\" where they can be copied to the clip board\n" .
		"but not seen. Provide the -f option to show passwords.\n" .
		"Use the -a option to see create and modified times, and\n" .
		"the index of the icon set for the entry.\n" .
		"",
             minargs => 1, maxargs => 3,
             args => \&complete_groups_and_entries,
             method => \&cli_show,
         },
         "otp" => {
             desc => "Show one-time password: otp <entry path|number>",
             doc => "\n" .
		"The otp command calculates and shows a one-time\n" .
		"password for the entry. Only Google Authenticator style\n" .
		"TOTPs are currently supported (TOTP per RFC 6238).\n" .
		"https://en.wikipedia.org/wiki/Google_Authenticator\n" .
		"\n" .
		"To configure an entry for this feature, place a line in\n" .
		"in the entry's Comments, as follows:\n" .
		"\n" .
		"2FA-TOTP: TheBase32SecretKeyProvided\n" .
		"\n" .
		"Alternatively, with KDBX4 files, the set command for field\n" .
		"\"otp\" will set an entry's Base32 encoded TOTP secret and in\n" .
		"a manner compatible with both kpcli and KeePassXC.\n" .
		"\n" .
		"The show command also provides OTPs for those entries.\n" .
		"The show command redacts 2FA secrets from the Comments\n" .
		"unless both the -a and -f flags are given.\n" .
		"",
             minargs => 1, maxargs => 3,
             args => \&complete_groups_and_entries,
             method => \&cli_otp,
         },
         "edit" => {
             desc => "Edit an entry: edit <path to entry|entry number>",
             doc => "\n" .
		"The edit command is used to modify an entry.\n" .
		"\n" .
		"Usage is straightforward.\n" .
		"\n" .
		$doc_passwd_gen .
		"",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { run_no_TSTP(\&cli_edit, @_); },
         },
         "attach" => {
             desc => "Manage attachments: attach <path to entry|entry number>",
             doc => "\n" .
		"The attach command provided an interactive user interface\n" .
		"for managing file attachments on an entry.\n" .
		"",
             minargs => 1, maxargs => 1,
             args => \&complete_groups_and_entries,
             method => sub { run_no_TSTP(\&cli_attach, @_); },
         },
         "mv" => {
             desc => "Move an item: mv <path to a group|or entries> <path to group>",
             minargs => 2, maxargs => 2,
             args => [\&complete_groups_and_entries, \&complete_groups],
             method => \&cli_mv,
         },
         "rename" => {
             desc => "Rename a group: rename <path to group>",
             minargs => 1, maxargs => 1,
             args => \&complete_groups,
             method => \&cli_rename,
         },
         "copy" => {
             desc => "Copy an entry: copy <path to entry> <path to new entry>",
             minargs => 2, maxargs => 2,
             args => [\&complete_groups_and_entries,
					\&complete_groups_and_entries],
             method => \&cli_copy,
         },
         "cp" => { alias => "copy", },
         "clone" => {
             desc =>"Clone an entry: clone <path to entry> <path to new entry>",
             doc => "\n" .
		"Clones an entry for you to edit. Similar to doing\n" .
		"\"cp foo bar; edit bar\" if that were possible.\n" .
		"\n",
             minargs => 2, maxargs => 2,
             args => [\&complete_groups_and_entries,
					\&complete_groups_and_entries],
             method => sub { run_no_TSTP(\&cli_clone, @_); },
         },
         "save" => {
             desc => "Save the database to disk",
             minargs => 0, maxargs => 0, args => "",
             method => sub { run_no_TSTP(\&cli_save, @_); },
         },
         "passwd" => {
             desc => "Change the opened database's password",
             minargs => 0, maxargs => 0, args => "",
             method => sub { run_no_TSTP(\&cli_passwd, @_); },
         },
         "close" => {
             desc => "Close the currently opened database",
             minargs => 0, maxargs => 0, args => "",
             method => sub { run_no_TSTP(\&cli_close, @_); },
         },
         "find" => {
             desc => "Finds entries",
             doc => "\n" .
		"Searches for entries with the given search term\n" .
		"in their title and places matches into \"/$FOUND_DIR/\".\n" .
		"\n" .
		"Add -a to search data fields beyond just the title:\n" .
		"  * " . join(", ", @ALL_FIND_FIELDS) . "\n" .
		"\n" .
		"Use -expired to find expired entries.\n",
             minargs => 1, maxargs => 2, args => "<search string>",
             method => \&cli_find,
         },
         "purge" => {
             desc => "Purges entries in a given group based on criteria.",
             doc => "\n" .
		"Purges entries within a given group based on the age of\n" .
		"the created, accessed, modified, or expiration fields.\n" .
		"\n" .
		"purge <path to a group>\n" .
		"\n" .
		"Add -r to recurse subgroups.\n" .
		"\n" .
		"Add --no-recycle to not copy purged entries to the\n" .
		"/Backup or \"/Recycle Bin\" groups.\n",
             minargs => 1, maxargs => 3, args => \&complete_groups_and_entries,
             method => \&cli_purge,
         },
         "pwd" => {
             desc => "Print the current working directory",
             maxargs => 0, method => \&cli_pwd,
         },
         "utf8" => {
             desc => "Turn UTF-8 support on or off.",
             method => \&cli_utf8,
             maxargs => 1, minargs =>0, args => [ sub {return [qw(status on off)];}, ],
         },
         "utf" => { alias => "utf8", },
         "icons" => {
             desc => "Change group or entry icons in the database",
             maxargs => 0,
             proc => sub { run_no_TSTP(\&cli_icons, @_); },
         },
       },
    );
$term->prompt(\&term_set_prompt);
#$term->{debug_complete} = 3;

# This allows the installing of code into any/all command methods.
# It is used here to insert PrintSupportMessage() into all commands.
my $commands = $term->commands();
CMD: foreach my $cmd (sort keys %{$commands}) {
  # If we're operating in --command mode, don't insert messages
  # requesting support so as to not complicate expect scripts.
  if (defined($opts->{command})) { last CMD; }
  METHOD: foreach my $proc_or_meth (qw(proc method)) {
    my $method = $commands->{$cmd}->{$proc_or_meth};
    #print "LHHD: $cmd $proc_or_meth ref: " . ref($method) . "\n";
    if (ref($method) ne 'CODE') { next METHOD; } # Only alter CODE
    if ($cmd eq 'quit') {
      next CMD; # We handle PrintSupportMessage() inside of cli_quit()
    }
    # If we get this far, insert the PrintSupportMessage() code
    my $new_code = sub { my $rv=&$method(@_); PrintSupportMessage(); $rv; };
    $commands->{$cmd}->{$proc_or_meth} = $new_code;
  }
}
$term->commands($commands);
#die Dumper($commands) . "\n";

# Seed our state global variable
our $state={
	'appname' => $APP_NAME,
	'term' => $term,
	'OPTIONAL_PM' => \%OPTIONAL_PM,
	'kdb_has_changed' => 0,
	'last_ls_ents' => [], # Array of entries last listed to the user.
	'put_master_passwd' => \&put_master_passwd,
	'get_master_passwd' => \&get_master_passwd,
	'last_activity_time' => 0, # initilized by setup_timeout_handling()
	'pwck_module' => load_pwck_module(),
	};
# If given --kdb=, open that file
if (defined($opts->{kdb}) && length($opts->{kdb})) {
  my $err = open_kdb($opts->{kdb}, $opts->{key}); # Sets $state->{'kdb'}
  if (length($err)) {
    print "$err\n";
    exit -1; # We exit if we failed to load the --kdb file
  }
} else {
  new_kdb($state);
}

# Enter the interative kpcli shell session
if (! defined($opts->{command})) {
  print "\n" .
	"KeePass CLI ($APP_NAME) v$VERSION is ready for operation.\n" .
	"Type 'help' for a description of available commands.\n" .
	"Type 'help <command>' for details on individual commands.\n";
}
if ($DEBUG) {print 'Using '.$term->{term}->ReadLine." for readline.\n"; }
if ( (! $DEBUG) && (lc($OSNAME) !~ m/^mswin/) &&
		($term->{term}->ReadLine ne 'Term::ReadLine::Gnu')) {
  print color('yellow') . "\n" .
	"* NOTE: You are using " . $term->{term}->ReadLine . ".\n" .
	"  Term::ReadLine::Gnu will provide better functionality.\n" .
	color('clear');
}
# My patch made it into Term::ShellUI v0.9, but I still chose not to make
# this program demand >=0.9 and instead look for the add_eof_exit_hook()
# and use it if it exists and warn if not.
if (Term::ShellUI->can('add_eof_exit_hook')) {
  $term->add_eof_exit_hook(\&eof_exit_hook);
} else {
  warn "* Please upgrade Term::ShellUI to version 0.9 or newer.\n";
}
print "\n";

setup_signal_handling();  # Exactly what the name indicates...

# Setup the inactivity timeout feature (--timeout).
if (defined($opts->{timeout}) && int($opts->{timeout}) > 0) {
  if  (! is_loaded('Sub::Install')) {
    print "Error: --timeout requires the Sub::Install module.\n";
    exit;
  }
  setup_timeout_handling();
}

if ( defined($opts->{command}) && ref($opts->{command}) eq 'ARRAY') {
  foreach my $cmd (@{$opts->{command}}) {
    $term->process_a_cmd($cmd);
  }
  &cli_quit($term,undef); # Needed else we leave a foo.lock file behind
} else {
  $term->run();
}

exit;

############################################################################
############################################################################
############################################################################

# This function sets the binmode for STDIO based on the setting of NO_UTF8
sub set_stdio_binmode {
  # I am unsure about having STDIN in this list, but think that is best.
  my @stdios = qw(STDOUT STDERR STDIN); # The STDIO file handle names
  # Pull and store the original STDIO PerlIO layers into a state (static)
  # variable so that they can be restored later.
  CORE::state $orig_stdio_layers = undef;
  if (! defined($orig_stdio_layers)) {
    $orig_stdio_layers = {};
    for my $io ( @stdios ) {
      my @layers = PerlIO::get_layers($io);
      $orig_stdio_layers->{$io} = join(':', @layers);
    }
  }
  #print "LHHD: ".Dumper($orig_stdio_layers)."\n";
  # Not sure which of these is best. Both seem to work...
  #my $utf8_layers = ":utf8";           # Expect UTF-8
  my $utf8_layers = ":encoding(UTF-8)"; # Do UTF-8 encoding
  # Loop through @stdios setting the binmode() appropriately
  for my $io ( @stdios ) {
    my $layers = undef;
    if ($NO_UTF8) {
      $layers = $orig_stdio_layers->{$io};
    } else {
      $layers = $utf8_layers;
    }
    #warn "LHHD: setting: binmode($io, $layers)\n";
    binmode($io, $layers);
  }
  # The binmode() calls just above seem to have an equivalent positive impact
  # as "use open ':locale';" (which I started with) without having to add open
  # as a dependency (requires perl-open.noarch on Fedora);
  #use open ':locale';            # all I/O with current locale
}

# These $path variables (almost) always come directly from Term::ShellUI user
# input and so they are not utf8 encoded, and need to be prior to printing.
# This message is also repeated in many places so this function allows for
# having a consistent message and for the utf8 upgrade of the $path.
sub no_entry_at_path_msg {
  my $path = shift @_;
  my $utf8_path = decode_if_not_utf8($path) if ($ALL_USER_INPUT_TO_UTF8);
  return "See no entry at path: $utf8_path\n";
}

sub open_kdb {
  my $file=shift @_;
  my $key_file=shift @_;
  my $password=shift @_ || undef;
  our $state;

  # Make sure the file exists, is readable, and is a keepass file
  if (! -f $file) {
    return "File does not exist: $file";
  }
  if (! -r $file) {
    return "File is not readable: $file";
  }
  if (magic_file_type($file) ne 'keepass') {
    return "Does not appear to be a KeePass file: $file";
  }

  my $KDB_module = 'File::KeePass';
  my $finf = kp_file_info($file);
  #warn "LHHDhdr: ".Dumper($finf)."\n";
  if ($finf->{version} == 2 and $finf->{kdbx_ver} >= 4.0) {
    $KDB_module = 'File::KDBX';
    if  (! (is_loaded($KDB_module) )) {
      my $msg = color('yellow') .
	"Perl module $KDB_module is required for KDBX4 support.\n".
	"Without it, KDBX4 files can only be imported.\n" .
	color('clear') .
	" - To import a KDBX v4 file, use the import command.\n" .
	" - For details, see: help import\n" .
	"";
      return $msg;
    }
  }

  # Look for lock file and warn if it is found
  my $lock_file = $file . '.lock'; # KeePassX style
  if (-f $lock_file &&
		! (defined($opts->{readonly}) && int($opts->{readonly})) ) {
    print color('bold yellow') .
	"WARNING:" .
	color('clear') . color('red') .
	       " A KeePassX-style lock file is in place for this file.\n" .
		"         It may be opened elsewhere." .
		" " . color('bold yellow') . "Be careful of saving!\n" .
	color('clear');
  } else {
    $state->{placed_lock_file} = $lock_file;
  }

  my $master_pass;
  if (defined($password) && length($password)) {
    $master_pass = $password;
  } elsif ( defined($opts->{pwfile}) ) {
    # Read the master password from the given file
    open(my $pwdfile, '<', $opts->{pwfile});
    $master_pass=<$pwdfile>;
    chomp $master_pass;
    close($pwdfile);
    $opts->{pwfile} = undef; # Only want to do this once!
  } else {
    # Ask the user for the master password and then open the kdb
    $master_pass=GetMasterPasswd();
  }
  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # With v3.6, we started doing extended error catching and reporting here.
  # KeePass has added new features to the kdbx v2 file format that are
  # referred to as "KDBX 4" and File::KeePass cannot open those files.
  # https://keepass.info/help/kb/kdbx_4.html
  # https://bugzilla.redhat.com/show_bug.cgi?id=1820134
  my @load_db_warns;
  my $kdb_obj = undef;
  if ($KDB_module eq 'File::KeePass') {
    my $comp_master_key = composite_master_pass('File::KeePass', $master_pass, $key_file);
    $kdb_obj = File::KeePass->new;
    if (! eval { local $SIG{__WARN__} = sub { push @load_db_warns, @_; };
		$kdb_obj->load_db($file, $comp_master_key) }) {
      my $errmsg = "Couldn't load the file $file\n\n" .
		"Error(s) from File::KeePass:\n$@";
      if (scalar(@load_db_warns)) {
        $errmsg .= "\nWarning(s) from File::KeePass:\n";
        my @warns = map {
		my $t = $_;
		$t =~ s/[^[:print:]]+//g;
		$t =~ s/(Found an unknown header type) \((\d+).+$/$1: $2/;
		$t; } @load_db_warns;
        $errmsg .= " - " . join("\n - ", @warns) . "\n";
      }
      return $errmsg;
    }
    $state->{kdb} = $kdb_obj;
  } elsif ($KDB_module eq 'File::KDBX') {
    my $comp_master_key = composite_master_pass('File::KDBX', $master_pass, $key_file);
    $kdb_obj = File::KDBX->new;
    if (! eval { $kdb_obj->load_file($file, $comp_master_key); }) {
      my $error = File::KDBX::Error->error($@);
      my $details = $error->details;
      #print Dumper($details)."\n";
      if (defined($error->{error})) {
        return "Errors from File::KDBX:\n$error->{error}\n";
      }
    }
    $state->{kdb} = $kdb_obj;
  } else {
    # Should be impossible
  }

  if (defined($state->{placed_lock_file})) {
    touch_file($state->{placed_lock_file});
  }

  # We hold a read file handle open for no reason other than
  # to show up in lsof.
  if (defined($state->{kdb_file_handle})) {
    close $state->{kdb_file_handle};
  }
  $state->{kdb_file_handle} = new FileHandle;
  open($state->{kdb_file_handle}, '<', $file);

  $state->{kdb_file} = $file;
  $state->{key_file} = $key_file;
  $state->{kdb_ver} = $finf->{version};
  if (defined($finf->{kdbx_ver})) {
    $state->{kdbx_ver} = $finf->{kdbx_ver};
  }

  # If not in NO_UTF8 mode, decode KDBv1 files to UTF8 strings
  if (! $NO_UTF8) {
    # This subroutine requires $state->{kdb_ver} and that is set just above.
    utf8_change_strings_KDBv1($state, 'decode'); # Decode to utf8
  }

  $state->{put_master_passwd}($master_pass);
  $state->{kdb_has_changed}=0;
  $master_pass="\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0";

  # Build the %all_grp_paths_fwd and %all_grp_paths_rev structures
  refresh_state_all_paths();
  $state->{last_ls_ents} = []; # Wipe the ls slate clean

  # Store the md5sum of the file so we can watch for unexpected changes
  $state->{kdb_file_md5} = Digest::file::digest_file_hex($file, "MD5");

  # Initialize our state into "/"
  cli_cd($term, {'args' => ["/"]});

  #print "LHHD: ".Dumper($state->{kdb})."\n";

  return ''; # If we return anything else it is an error message
}

# Called by Term::ShellUI to get the user prompt
sub term_set_prompt($$) {
  my $term=shift @_;
  my $raw_cmd=shift @_;
  our $state;

  my $app=$state->{appname};
  my $pwd=get_pwd();
  return "$app:$pwd> ";
}

# Map legacy File::KeePass key names that differ to
# those used in File::KDBX.
sub KeePass_KDBX_key_map {
  my $module_name = shift @_ || 'File::KeePass';
  my $km = {
    'File::KeePass' => {
	title	=> 'title',
	id	=> 'id',
	},
    'File::KDBX' => {
	title	=> 'name',
	id	=> 'uuid',
	},
  };
  if (! defined($km->{$module_name})) {
    die "FATAL ERROR: KeePass_KDBX_key_map(): unknown module_name=$module_name\n";
  }
  return %{$km->{$module_name}};
}

# Walks through a tree of groups building a flat hash of NULL-separated
# paths to group IDs. Called on the root to build a full path tree.
sub build_all_group_paths {
  my $hash = shift @_;
  my $g = shift @_;
  my $root_path = shift @_ || [];
  our $state;

  # In the initial call (not the recursion), we are
  # first handed a File::KDBX::Iterator object from
  # $state->{kdb}->groups. Later calls in the recursion
  # are simple arrays.
  if (ref($g) eq 'File::KDBX::Iterator') {
    # https://metacpan.org/release/MICHAEL/Iterator-Simple-0.07/view/lib/Iterator/Simple.pm
    # $g = $g->to_array(); # Wrong, but not 100% sure why yet.
    # NOTE: This takes just the top group off of the list!
    # This is different behavior than for File::KeePass and
    # I don't yet fully understand why, but I do know that
    # the KDBX file format only allows one root group.
    my @tmp = $g->();
    $g = \@tmp;
  }
  #warn "LHHg: ".Dumper($root_path, 'size of $g', scalar(@{$g}))."\n";

  foreach my $me (@{$g}) {
    #print "LHHD: ref(\$g): ".ref($g)."\n";
    my @path_to_me = @{$root_path};
    # For tab completion to work correctly, we cannot place utf8 strings
    # in our paths, thus we ask getLabel() to encode for us if needed.
    my $title = getLabel($me, 1);
    push @path_to_me, $title;
    my $path=join("\0",@path_to_me);
    my $err_path = '/' . humanize_path($path);
    if (defined($hash->{$path})) {
      print color('bold yellow') .  "WARNING: " . color('clear') .
        color('red') . "Multiple groups titled: $err_path!\n" .
        color('red') . "This is unsupported and may cause data loss!\n" .
        color('clear');
    }
    $hash->{$path}=getID($me);

    #print "LHHD: for ".Dumper($path, \@path_to_me)."\n";
    if (defined($me->{groups})) {
      build_all_group_paths($hash,$me->{groups},\@path_to_me);
    }
  }
  return (scalar(keys(%{$hash})));
}

# Walks through a tree of groups building a flat hash of NULL-separated
# paths to entry IDs. Called on the root to build a full path tree.
sub build_all_entry_paths {
  my $hash = shift @_;
  my $g = shift @_;
  my $root_path = shift @_ || [];

  my $red=color('red');

  # In the initial call (not the recursion), we are
  # first handed a File::KDBX::Iterator object from
  # $state->{kdb}->groups. Later calls in the recursion
  # are simple arrays.
  if (ref($g) eq 'File::KDBX::Iterator') {
    # https://metacpan.org/release/MICHAEL/Iterator-Simple-0.07/view/lib/Iterator/Simple.pm
    # $g = $g->to_array(); # Wrong, but not 100% sure why yet.
    # NOTE: This takes just the top group off of the list!
    # This is different behavior than for File::KeePass and
    # I don't yet fully understand why, but I do know that
    # the KDBX file format only allows one root group.
    my @tmp = $g->();
    $g = \@tmp;
  }

  foreach my $me (@{$g}) {
    my @path_to_me = @{$root_path};
    # For tab completion to work correctly, we cannot place utf8 strings
    # in our paths, thus we ask getLabel() to encode for us if needed.
    my $title = getLabel($me, 1);
    push @path_to_me, $title;
    #warn "LHHD: title = $title\n";
    #warn "LHHD: me = ".Dumper($me)."\n";
    my %dupes = ();
    if (defined($me->{entries})) {
      ENTRY: foreach my $ent (@{$me->{entries}}) {
        # NOTE: Be *sure* to only use getLabel() here!!!
        # As of 06-Aug-2022, we are setting ->{title} in
        # get_entry_by_uuid() (among other things),
        # (which File::KDBX does not provide) and with cli_edit, that
        # created a major headache when the "title" didn't appear to
        # be changing. I intend to make sure that I expunge all
        # cases where we're setting ->{title} for File::KDBX, but
        # it's not done yet.
        # For tab completion to work correctly, we cannot place utf8 strings
        # in our paths, thus we ask getLabel() to encode for us if needed.
        my $ent_title = getLabel($ent, 1);
        my $ent_uname = get_username($ent);
        #warn "LHHD: title/username = $ent_title / $ent_uname\n";
        if ($ent_title eq 'Meta-Info' && $ent_uname eq 'SYSTEM') {
          next ENTRY; # skip Meta-Info/SYSTEM entries
        }
        my $path=join( "\0", (@path_to_me, $ent_title) );
        my $err_path = '/' . humanize_path($path);
        # warn "LHHD: $err_path\n";
        if ($ent_title eq '') {
          print color('bold yellow') . "WARNING: " . color('clear') .
                $red . "There is an entry with a blank title in $err_path!\n" .
                color('clear');
        }
        # As of kpcli 4.0, I attempt to support multiple entries with the same
        # name being in a group and so no longer throw this warning. I am
        # leaving it commented out for now, in case I must revert.
        #my $bugrp_id = get_recycle_group_uuid($state, 0); # "Recycle Bin"
        #my $parent_group = get_parent_group_of_uuid($state->{kdb}, getID($ent));
        #if (defined($hash->{$path}) && (getID($parent_group) ne $bugrp_id)) {
        #  print color('bold yellow') . "WARNING: " . color('clear') .
        #        $red . "Multiple entries titled: $err_path!\n" .
        #        $red . "This is unsupported and may cause data loss!\n" .
        #        color('clear');
        #}
        # Handle duplicates
        $dupes{$path}++;
        if ($dupes{$path} > 1) {
          # If the first one we saw is still in place, move it to "-01"
          if (defined($hash->{$path})) {
            my $tmp_path = $path;
            $tmp_path .= sprintf($DUP_ENTRIES_FORMAT, 1);
            $hash->{$tmp_path} = $hash->{$path};
            delete $hash->{$path};
          }
          $path .= sprintf($DUP_ENTRIES_FORMAT, $dupes{$path});
        }
        $hash->{$path}=getID($ent);
      }
    }

    if (defined($me->{groups})) {
      build_all_entry_paths($hash,$me->{groups},\@path_to_me);
    }
  }
  return (scalar(keys(%{$hash})));
}

# Returns the current path the user is sitting in.
sub get_pwd {
  my $pwd='';
  if (defined($state->{path}->{id}) &&
	defined($state->{all_grp_paths_rev}->{$state->{path}->{id}})) {
    $pwd=$state->{all_grp_paths_rev}->{$state->{path}->{id}};
  }
  $pwd =~ s%/%\\/%g;
  $pwd =~ s/\0/\//g;
  $pwd = '/' . $pwd;
return $pwd;
}

# Destroys our /_found group (where we place search results)
sub destroy_found {
  our $state;
  # Look for an exising /_found and kill it if it exists
  my $k=$state->{kdb};

  if (! (defined($state->{found_path}) && defined($state->{found_gid}))) {
    return 0; # Nothing to do
  }

  my $found_group = get_group_by_uuid($state->{kdb}, $state->{found_gid});

  if (defined($found_group)) {
    if (ref($k) eq 'File::KeePass') {
      my @oldents = $k->find_entries({group_id => getID($found_group)});
      foreach my $ent (@oldents) {
        $k->delete_entry({id => getID($ent)});
      }
      $k->delete_group({level=>0,title=>$FOUND_DIR});
    } elsif (ref($k) eq 'File::KDBX') {
      my $root_grp = $k->root;
      my $removed_group = $root_grp->remove_group($found_group);
      if (getID($removed_group) ne getID($found_group)) {
        warn "ERROR: apparent bug in destroy_found().\nremoved_group=$removed_group";
      }
    }
  }

  # Because we destroyed /_found we must refresh our $state paths
  refresh_state_all_paths();
}

# Refreshes $state->{all_grp_paths_fwd} and $state->{all_grp_paths_rev}
sub refresh_state_all_paths() {
  our $state;

  my $groups = [];
  if (ref($state->{kdb}) eq 'File::KDBX') {
    @{$groups} = ( $state->{kdb}->root );
  } elsif (ref($state->{kdb}) eq 'File::KeePass') {
    $groups = $state->{kdb}->groups;
  }

  # Build all group paths
  my %all_grp_paths_fwd;
  build_all_group_paths(\%all_grp_paths_fwd,$groups);
  my %all_grp_paths_rev = reverse %all_grp_paths_fwd;
  $state->{all_grp_paths_fwd}=\%all_grp_paths_fwd;
  $state->{all_grp_paths_rev}=\%all_grp_paths_rev;
  #print "LHHD: ".Dumper($state->{all_grp_paths_fwd},$state->{all_grp_paths_rev})."\n";

  # Build all entry paths
  my %all_ent_paths_fwd;
  build_all_entry_paths(\%all_ent_paths_fwd,$groups);
  my %all_ent_paths_rev = reverse %all_ent_paths_fwd;
  $state->{all_ent_paths_fwd}=\%all_ent_paths_fwd;
  $state->{all_ent_paths_rev}=\%all_ent_paths_rev;
  #print "LHHD: ".Dumper($state->{all_ent_paths_fwd},$state->{all_ent_paths_rev})."\n";

  # Sanity check entry paths versus groups. This is primarily here to catch
  # bugs that may be introduced.
  foreach my $ep (sort keys %all_ent_paths_fwd) {
    my @pieces = split("\0", $ep);
    my $entry_name = pop @pieces;  # Pop off the entry itself
    my $group_path = join("\0", @pieces);
    if (! defined($all_grp_paths_fwd{$group_path})) {
      warn "Entry \"$entry_name\" is in a missing path: /" .
					humanize_path($group_path)."\n";
    }
  }
}

# Returns the list of root-level groups.
# In KDBX4, this will be a one item list.
sub get_root_groups {
  my $k = shift @_;
  my @root_groups = ();
  if (ref($k) eq 'File::KeePass') {
    @root_groups = $k->find_groups({level=>0}); # All root-level groups
  } elsif (ref($k) eq 'File::KDBX') {
    $root_groups[0] = $k->root; # Only one root in KDBXv4
  } else {
    warn "get_root_groups() called with invalid \$state->{kdb}!\n";
  }
  return @root_groups;
}

# Returns a list of all groups.
sub get_all_groups {
  my $k = shift @_;
  my @groups = ();
  if (ref($k) eq 'File::KeePass') {
    @groups = $k->find_groups({});
  } elsif (ref($k) eq 'File::KDBX') {
    my $iterator = $k->groups();
    @groups = @{ $iterator->to_array() };
  } else {
    warn "get_all_groups() called with invalid \$state->{kdb}!\n";
  }
  return @groups;
}
# Returns a list of all entries.
sub get_all_entries {
  my $k = shift @_;
  my @entries = ();
  if (ref($k) eq 'File::KeePass') {
    @entries = $k->find_entries({});
  } elsif (ref($k) eq 'File::KDBX') {
    my $iterator = $k->entries();
    @entries = @{ $iterator->to_array() };
  } else {
    warn "get_all_entries() called with invalid \$state->{kdb}!\n";
  }
  return @entries;
}

# This function takes a group ID and returns all of the child
# groups of that group, flattened.
sub all_child_groups_flattened {
  my $group_id=shift @_;
  our $state;

  my $k=$state->{kdb};
  my @groups=();
  if (defined($state->{all_grp_paths_rev}->{$group_id})) {
    my $grp_path = $state->{all_grp_paths_rev}->{$group_id};
    my @chld_grp_paths = grep(/^$grp_path/, keys %{$state->{all_grp_paths_fwd}});
    foreach my $chld_grp_path (@chld_grp_paths) {
      my $chld_grp_uuid = $state->{all_grp_paths_fwd}->{$chld_grp_path};
      next if ($chld_grp_uuid eq $group_id); # Only want this group's children
      my $chld_grp = get_group_by_uuid($k, $chld_grp_uuid);
      push @groups, $chld_grp;
    }
  }

  return @groups;
}

# A function to properly sort entries by title
sub entry_sort($$) {
  my $a=shift @_;
  my $b=shift @_;
  return ncmp(getLabel($a),getLabel($b));
}

# A function to properly sort groups by title
sub group_sort($$) {
  my $a=shift @_;
  my $b=shift @_;

  my $ROOT_LEVEL = 0; # KDBv1 and KDBX3
  if (ref($state->{kdb}) eq 'File::KDBX') {
    $ROOT_LEVEL = 1; # Because KDBX4 files have a single root group
  }

  # $ROOT_LEVEL special cases ###############################################
  # NOTE: The higher in these lists the group is, the lower it sorts.
  # Currently, when all of these exist, the sort order is:
  # ...
  # _autosaves/
  # _found/
  # Recycle Bin/
  my $level_a = get_level($a);
  my $level_b = get_level($b);
  # Recycle and _found dirs are special cases
  my @bottom_grps = (get_recycle_group_uuid($state), $state->{found_gid});
  foreach my $grp_gid (@bottom_grps) {
    next if (! defined($grp_gid));
    if (      $grp_gid eq getID($a) && $level_a == $ROOT_LEVEL) {
      return 1;
    } elsif ( $grp_gid eq getID($b) && $level_b == $ROOT_LEVEL) {
      return -1;
    }
  }
  # AUTOSAVES_DIR is a special case
  if (      $AUTOSAVES_DIR eq getLabel($a) && $level_a == $ROOT_LEVEL) {
    return 1;
  } elsif ( $AUTOSAVES_DIR eq getLabel($b) && $level_b == $ROOT_LEVEL) {
    return -1;
  }
  ###########################################################################

  # Sort everything else naturally (Sort::Naturally::ncmp).
  return ncmp(getLabel($a),getLabel($b));
}

# -------------------------------------------------------------------------
# All of the cli_*() functions are below here
# -------------------------------------------------------------------------

# A simple wrapper function to block SIGTSTP (^Z) during certain commands.
# This is not available on Windows, thus the if(defined()) calls.
sub run_no_TSTP {
  my $func = shift @_;
  if (defined($SIG{TSTP})) { $SIG{TSTP}='IGNORE'; }
  my @retval = &$func(@_);
  if (defined($SIG{TSTP})) { $SIG{TSTP}='DEFAULT'; }
  return @retval;
}

# pwck-related subroutines
sub get_pwck_module {
  our $state;
  if (defined($state->{pwck_module})) {
    return $state->{pwck_module};
  }
  return undef;
}

# The list of pwck modules that kpcli supports, listed in the
# order of preference. The first found installed will be used.
sub get_pwck_module_list {
  my @pwckModules = qw(
	Data::Password::zxcvbn
	Data::Password::passwdqc
	Data::Password
	);
  return @pwckModules;
}

sub load_pwck_module {
  my $self = shift @_;

  if (defined(get_pwck_module())) {
    return 0; # Nothing to do. Already loaded.
  }

  # Try to load one of the optional modules needed by this feature.
  # This list is in order of preference.
  my @pwckModules = get_pwck_module_list();
  pwckModules: foreach my $pwckmod (@pwckModules) {
    # If it's already loaded then bail out now
    if (is_loaded($pwckmod)) { return $pwckmod; }
    # Try to load it. If we succeed, bail out
    if (runtime_load_module(\%OPTIONAL_PM,$pwckmod,undef)) {
      if ($pwckmod eq 'Data::Password::passwdqc') {
        no warnings 'once'; # These are intentionally only used once
        $Data::Password::passwdqc::max=999; # Max password length allowed
        $Data::Password::passwdqc::min=[INT_MAX, 20, 11, 8, 7]; # man pwqcheck
      } elsif ($pwckmod eq 'Data::Password') {
        no warnings 'once'; # These are intentionally only used once
        $Data::Password::MINLEN = 8;
        $Data::Password::MAXLEN = 0;
      }
      return $pwckmod;
    }
  }
  return undef;
}

sub cli_utf8 {
  my $self = shift @_;
  my $params = shift @_;
  my $on_or_off = $params->{args}->[0] // 'status';
  if (lc($on_or_off) eq 'status') {
    my $status = $NO_UTF8 ? 'off' : 'on';
    print "$status\n";
    return 0;
  }
  $NO_UTF8 = 0; # Assume "utf8 on"
  $NO_UTF8 = 1 if (lc($on_or_off) eq 'off'); # Turn it off if asked to
  set_stdio_binmode(); # Set the STDIO binmode

  # Flip the UTF8 status of KDBv1 files if needed
  my $action = 'decode';
  $action = 'encode' if ($NO_UTF8);
  utf8_change_strings_KDBv1($state, $action); # En/Decode utf8

  refresh_state_all_paths(); # In case we UTF-8 flipped a KDBv1 file
}

# Checks passwords for their quality
sub cli_pwck {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  my $pwckMethod = get_pwck_module();

  # If we have no pwck module loaded, let the user know and bail out
  if (! defined($pwckMethod)) {
    my $modsV = " - " . join("\n - ", get_pwck_module_list());
    print "Error: pwck requires one of these modules:\n$modsV\n";
    return;
  }

  # Tell the user which module we are using for password testing.
  print "Using perl module $pwckMethod for password testing...\n\n";

  my @targets = ();
  my $target = $params->{args}->[0];
  # Start by trying to find a single entity with the paramter given.
  # If no single entity is found then try to find entities based on
  # assuming that the path given is a group.
  my $ent=find_target_entry_by_number_or_path($target);
  if (defined($ent)) {
    push @targets, $ent;
  } else {
    my $k = $state->{kdb};
    my @groups = ();
    my $target = normalize_path_string($target);
    if ($target eq '' || $target eq '.' && get_pwd() eq '/') {
      @groups = get_all_groups($k); # Every group in the file!
    } elsif (defined($state->{all_grp_paths_fwd}->{$target})) {
      my $group_id = $state->{all_grp_paths_fwd}->{$target};
      @groups = all_child_groups_flattened($group_id);
      # Push this group onto its children (inclusive)
      push @groups, get_group_by_uuid($k, $group_id);
    }
    # Loop over each target group adding each of its entries as targets
    foreach my $group (@groups) {
      my ($grps, $ents) = get_kids_by_group_uuid($k, getID($group));
      my @entries = @{$ents};
      {
        ENTRY: foreach my $ent (@entries) {
          # skip Meta-Info/SYSTEM entries
          if (getLabel($ent) eq 'Meta-Info' && get_username($ent) eq 'SYSTEM') {
            next ENTRY;
          }
          # If we don't have this entry recorded in all_ent_paths_rev then
          # we can't report on it. The only case known of is when we have
          # multiple entries at the same level (unsupported) and typically
          # that's only seen in /Backup in v1 databases.
          if (defined($state->{all_ent_paths_rev}->{getID($ent)})) {
            push @targets, $ent;
          } elsif (! (getLabel($group) eq 'Backup' && get_level($group) == 0)) {
            # TODO - can we do away with this check post v4.0, now that we
            # try to support multiple entries with the same name in a group?
            #warn "Warning: missing entry " . &Dumper($ent) . "\n";
            warn "Warning: missing entry\n";
            next;
          }
        }
      }
    }
  }

  # Test each password, collect the results and record empty passwords
  my %results=();
  my @empties = ();
  print "  working...\r";
  my @busy_chars = qw(\ | / -); my $i=0; my $in=10;
  foreach my $ent (@targets) {
    printf "%s\r", $busy_chars[int($i/$in)%($#busy_chars+1)] if (!($i++ % $in));
    my $pass = get_password($state->{kdb},$ent);
    if (length($pass) == 0) {
      push @empties, $ent;
      $results{getID($ent)} = '';
    } else {
      $results{getID($ent)} = my_IsBadPassword($pwckMethod, $pass);
    }
    # If the user hit ^C (SIGINT) then we need to stop
    if (recent_sigint()) {
       print "\r"; # Need to return to column 0 of the output line
       return 0;
    }
  }

  # If we only analyzed one password, return singular-style results
  if (scalar(@targets) == 1) {
    my $ent=$targets[0];
    if (length($results{getID($ent)})) {
      print "Password concerns: " . $results{getID($ent)} . "\n";
    } elsif (scalar(@empties) > 0) {
      print "Password field is empty.\n";
    } else {
      print "Password strength is good.\n";
    }
  } else {
  # If we analyzed more than one password, return multiple-style results
    my %problems=();
    foreach my $ent_id (keys %results) {
      if (length($results{$ent_id})) {
        $problems{$state->{all_ent_paths_rev}->{$ent_id}} = $ent_id;
      }
    }
    my $analyzed = scalar(@targets);
    my $problem_count = scalar(keys %problems);
    my $empty_count = scalar(@empties);
    print "$analyzed passwords analyzed, $empty_count blank, " .
					"$problem_count concerns found";
    if ($problem_count > 0) { print ":\n"; } else { print "."; }
    print "\n";
    foreach my $path (sort keys %problems) {
      print humanize_path($path) . ": $results{$problems{$path}}\n";
      if (! length(humanize_path($path))) {
        my $ent_id = $problems{$state->{all_ent_paths}->{$path}};
        my $ent = get_entry_by_uuid($state->{kdb}, $ent_id);
        #warn "LHHD: ".&Dumper($ent)."\n";
      }
    }
  }

  return 0;
}

# This function handles abstraction to mutiple password
# quality checking libraries.
sub my_IsBadPassword($) {
  my $pwckMethod = shift @_;
  my $pass = shift @_;

  my $result = undef;
  if ($pwckMethod eq 'Data::Password') {
    $result = Data::Password::IsBadPassword($pass);
    if (defined($result) && $result =~ m/dictionary word/i) {
      # IsBadPassword() reports dictionary words that it finds. I don't
      # like that from a security perspective so we change that here.
      $result = "contains a dictionary word";
    }
  } elsif ($pwckMethod eq 'Data::Password::passwdqc') {
    my $pwdqc = Data::Password::passwdqc->new;
    my $is_valid = $pwdqc->validate_password($pass);
    $result = $pwdqc->reason if not $is_valid;
  } elsif ($pwckMethod eq 'Data::Password::zxcvbn') {
    my $strength = Data::Password::zxcvbn::password_strength($pass);
    #print "LHHD: ".Dumper($strength)."\n";
    if ($strength->{score} < 3) {
      $result .= "Strength score is low at " . $strength->{score};
      if (defined($strength->{feedback}->{warning}) &&
		length($strength->{feedback}->{warning}) ) {
        $result .= "\nWarning: " . $strength->{feedback}->{warning};
      }
      if (defined($strength->{feedback}->{suggestions}) &&
		ref($strength->{feedback}->{suggestions}) eq 'ARRAY') {
        $result .= "\nSuggestions:\n" .
		" - " . join("\n - ", @{$strength->{feedback}->{suggestions}});
        $result .= "\n";
      }
    }
  }

  return $result;
}

# From File::KDBX::Util ###################################################
sub my_format_uuid {
    local $_    = shift // "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0";
    my $delim   = shift // '';
    #length($_) == 16 or throw 'Must provide a 16-bytes UUID', size => length($_), str => $_;
    length($_) == 16 or return 'invalid UUID';
    return uc(join($delim, unpack('H8 H4 H4 H4 H12', $_)));
}
sub my_uuid {
    local $_ = shift // return "\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0";
    s/-//g; # Strip delimeters
    #/^[A-Fa-f0-9]{32}$/ or throw 'Must provide a formatted 128-bit UUID';
    /^[A-Fa-f0-9]{32}$/ or return 'invalid UUID';
    return pack('H32', $_);
}
###########################################################################

# Prints some statistics about the open KeePass file
sub cli_stats {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # Group and entry counts
  my %stats;
  $stats{group_count} = scalar(keys(%{$state->{all_grp_paths_fwd}}));
  $stats{entry_count} = scalar(keys(%{$state->{all_ent_paths_fwd}}));

  # Password lengths
  my $k=$state->{kdb};
  my %password_lengths;
  print "  working...\r";
  my @busy_chars = qw(\ | / -); my $i=0; my $in=100;
  foreach my $ent_id (values(%{$state->{all_ent_paths_fwd}})) {
    printf "%s\r", $busy_chars[int($i/$in)%($#busy_chars+1)] if (!($i++ % $in));
    my $ent = get_entry_by_uuid($k, $ent_id);
    my $pass_len = length(get_password($state->{kdb},$ent));
    if ($pass_len < 1) {
      $password_lengths{"0"}++;
    } elsif ($pass_len > 0 && $pass_len < 8) {
      $password_lengths{"1-7"}++;
    } elsif ($pass_len > 7 && $pass_len < 12) {
      $password_lengths{"8-11"}++;
    } elsif ($pass_len > 11 && $pass_len < 17) {
      $password_lengths{"12-16"}++;
    } elsif ($pass_len > 16 && $pass_len < 20) {
      $password_lengths{"17-19"}++;
    } elsif ($pass_len > 19) {
      $password_lengths{"20+"}++;
    }
    # If the user hit ^C (SIGINT) then we need to stop
    if (recent_sigint()) {
       print " "x20 . "\r"; # Need to return to column 0 of the output line
       return 0;
    }
  }

  my $kdb_finf = undef;
  my $kdb_fname = 'N/A'; # N/A is it's a new, never saved file.
  if (defined($state->{kdb_file})) {
    $kdb_fname = $state->{kdb_file};
    $kdb_finf = kp_file_info($kdb_fname);
  }

  my $ftype = 'unknown';
  if (defined($state->{kdbx_ver})) {
    $ftype = 'KDBX v'.$state->{kdbx_ver};
  } elsif ($state->{kdb_ver}) {
    $ftype = 'KDB v'.$state->{kdb_ver};
  }

  # File::KeePass / File::KDBX
  my ($hdr, $dbname, $dbdesc) = (undef,undef,undef);
  my ($cipher,$rounds,$compression) = (undef,undef,undef);
  my ($iterations, $kdf_cipher, $generator) = (undef,undef,undef);
  if (ref($state->{kdb}) eq 'File::KeePass') {
    $hdr =    $k->{header};
    $dbname = $hdr->{database_name} // undef;
    $dbdesc = $hdr->{database_description} // undef;
    $cipher = $hdr->{cipher} // $hdr->{enc_type} // 'N/A';
    $rounds = $hdr->{rounds} // 'N/A';
    $compression = $hdr->{compression};
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    $hdr =    $k->headers;
    $dbname = $k->database_name // undef;
    $dbdesc = $k->database_description // undef;
    $generator = $k->generator // undef;
    $cipher = my_format_uuid($k->cipher_id,'-');
    # From File::KDBX::Cipher
    my %c = (
	'61AB05A1-9464-41C3-8D74-3A563DF8DD35'=>'AES128',
	'31C1F2E6-BF71-4350-BE58-05216AFC5AFF'=>'AES256',
	'D6038A2B-8B6F-4CB5-A524-339A31DBB59A'=>'ChaCha20',
	'716E1C8A-EE17-4BDC-93AE-A977B882833A'=>'Salsa20',
	'098563FF-DDF7-4F98-8619-8079F6DB897A'=>'Serpent',
	'AD68F29F-576F-4BB9-A36A-D47AF965346C'=>'Twofish',
	);
    if (defined($c{$cipher})) {
      $cipher = $c{$cipher};
    }
    $rounds = $k->transform_rounds;
    $compression = $k->compression_flags;
    # From File::KDBX::KDF
    my %kdf_ciphers = (
	'C9D9F39A-628A-4460-BF74-0D08C18A4FEA'=>'AES',
	'7C02BB82-79A7-4AC0-927D-114A00648238'=>'AES (challenge-response variant)',
	'EF636DDF-8C29-444B-91F7-A9A403E30A0C'=>'Argon2d',
	'9E298B19-56DB-4773-B23D-FC3EC6F0A1E6'=>'Argon2id',
	);
    my $kdf = $k->kdf_parameters;
    $iterations = $kdf->{I} if (exists($kdf->{I}));

    $kdf_cipher = my_format_uuid($kdf->{'$UUID'},'-');
    if (defined($kdf_ciphers{$kdf_cipher})) {
      $kdf_cipher = $kdf_ciphers{$kdf_cipher};
    }
  }

  # Label the compression, if the file has it
  $compression = ($compression ? 'gzip' : 'None');

  my $t= " "x20 . "\r" .
	"File: $kdb_fname\n";
  $t .= "Name: $dbname\n" if (defined($dbname) && length($dbname));
  $t .= "Type: $ftype\n" .
	"Key file: " .
	(defined($state->{key_file}) ? $state->{key_file} : 'N/A') . "\n" .
	"Module: ".ref($state->{kdb})."\n";
  if (defined($dbdesc) && length($dbdesc)) {
    my $desc = $dbdesc;
    $desc =~ s/[\r\n]/\n/g;
    my @l = split(/\n/, $desc);
    $t .= "Description:\n" . "| " . join("\n| ", @l) . "\n";
  }
  # KeePassXC does not set this, so I decided not to show it.
  #$t .= defined($generator) ? "Made By: $generator\n" : '';

  #my $meta = $k->meta; # Metadata
  #print "LHHD: " . Dumper($meta)."\n";

  $t .= "\n";
  $t .= "Cipher:               $cipher\n";
  $t .= "Rounds:               $rounds\n";
  if (defined($iterations)) {
    $t.="Iterations:           $iterations\n";
  }
  if (defined($kdf_cipher)) {
    $t.="KDF Cipher:           $kdf_cipher\n";
  }
  $t .= "Compression:          $compression\n";
  $t .= "Number of groups:     $stats{group_count}\n" .
	"Number of entries:    $stats{entry_count}\n";
  if (scalar(keys(%password_lengths))) {
    $t.="Entries with passwords of length:\n".
			stats_print(\%password_lengths)."\n";
  }
  print $t;
}

sub cli_cls {
  if (lc($OSNAME) =~ m/^mswin/ &&
		(! is_loaded('Win32::Console::ANSI'))) {
    system("cls");
  } else {
    print "\033[2J\033[0;0H";
    $|=1; # Needed for MS Windows (Win32::Console::ANSI works w/this flush)
  }
}

sub cli_pwd {
  my $pwd = decode_if_not_utf8(get_pwd());
  print "$pwd\n";
}

sub cli_cd {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  my $raw_pathstr = $params->{args}->[0];
  # "cd" -- no parameter is given, so go to "home" (/)
  if (! defined($raw_pathstr)) {
    return cli_cd($self, {'args' => ['/']});;
  }
  # "cd ."
  if ($raw_pathstr =~ m/^[.]$/) {
    return; # nothing to do
  }
  # "cd -"
  if ($raw_pathstr =~ m/^[-]$/) {
    return cli_cd($self, {'args' => [$state->{oldpwd}]});
  }
  # Everything else is handled by helpers
  return cli_cd_helper($state,normalize_path_string($raw_pathstr));
}

# Takes a possibly wacky path with ".."s and such and normalizes it into a
# NULL-separated path that can be used as a key into $state->{all_grp_paths_fwd}
sub normalize_path_string($) {
  my $path_string = shift @_;
  our $state;

  if (utf8::is_utf8($path_string)) {
    warn "normalize_path_string(\"$path_string\"): the \$path_string is_utf8. Likely a bug.\nPlease report it at https://sourceforge.net/p/kpcli/bugs/!\n";
    if ($DO_TRACE_DUMPS) { my $trace = Devel::StackTrace->new; print $trace->as_string; }
  }

  if ($path_string =~ m/\0/) {
    warn "normalize_path_string(\"$path_string\"): path contains a NULL. Likely a bug.\nPlease report it at https://sourceforge.net/p/kpcli/bugs/!\n";
  }

  # Split the path into @path
  # http://efreedom.com/Question/1-3588341/Implement-Escape-Sequence-Using-Split-Perl
  my $delim="/";
  my $escape="\\";
  my @path = $path_string =~
	/(?:\Q$delim\E|^)((?>(?:\Q$escape\E.|(?!\Q$delim\E).)*))/gs;
	#/(?:\Q$delim\E|^)((?:\Q$escape\E.|(?!\Q$delim\E).)*+)/gs; # perl 5.10+
  s/\Q$escape$delim\E/$delim/g for @path;
  @path=grep(!/^$/, @path); # Drop meaningless (excess) deimiters (/foo//bar)

  # This block handles absolute and relative paths
  my $path_str='';
  if ($path_string =~ m%^/%) { # Absolute path
    $path_str=join("\0",@path);
  } else { # Relative path
    my $pwd='';
    if (defined($state->{path}->{id}) && 
	defined($state->{all_grp_paths_rev}->{$state->{path}->{id}})) {
      $pwd = $state->{all_grp_paths_rev}->{$state->{path}->{id}};
    }
    my @nwd=split("\0", $pwd);
    push @nwd, @path;
    $path_str=join("\0", @nwd);
  }

  # We should now have a NULL-separated, fully qualified path and
  # we just need to work on cleaning up things like "." and ".."
  # Squash single dots
  while ($path_str=~s/\0[.]\0|^[.]\0|\0[.]$/\0/) {}
  # Kill ".." and their parents
  while ($path_str=~s/[^\0]+\0+[.][.]//) {}
  $path_str=~s/\0\0+/\0/g; # squash any adjacent delimeters
  $path_str=~s/^\0+//; # squash any leading delimeters
  $path_str=~s/\0+$//; # squash any trailing delimeters

  return $path_str;
}

sub cli_cd_helper($$) {
  my $state=shift @_;
  my $path_str=shift @_;
  if (defined($state->{all_grp_paths_fwd}->{$path_str})) {
    $state->{oldpwd} = get_pwd();
    my $id = $state->{all_grp_paths_fwd}->{$path_str};
    $state->{path}->{id} = $id;
    return 0;
  } elsif ($path_str eq '') { # cd /
    $state->{oldpwd}=get_pwd();
    # TODO - consider making this behavior optional.
    # Maybe --kdbx4root to disable it and a kdbx4root toggle command
    if (ref($state->{kdb}) eq 'File::KDBX' && $state->{kdbx_ver} >= 4.0) {
      # KDBX4 files have only one root node and so going to / is pointless
      my $id = $state->{all_grp_paths_fwd}->{$state->{kdb}->root->name};
      $state->{path}->{id} = $id;
    } else {
      delete $state->{path};
    }
    return 0;
  } else {
    print "Invalid path\n";
    return -1;
  }
}

# Return 1 if entry's password never expires, else 0.
# Helps support both v1 (*.kdb) and v2 (*.kdbx) files.
sub does_expire_never {
  my $kdb_ver = shift @_;
  my $ent = shift @_;
  my $expires = $ent->{expires};
  if ($kdb_ver == 1 && $expires =~ m/^(\d{4})-/ && ($1 == 2999)) {
    return 1;
  } elsif ($kdb_ver == 2 && (! $ent->{expires_enabled})) {
    return 1;
  }
  return 0;
}

# Helper function of cli_find() to find expired entries.
sub find_expired_entries {
  my $kdb_ver = shift @_;
  my $k = shift @_;
  our $state;

  my @expired = ();
  my @all_entries_flattened = get_all_entries($k);

  # The code below depends on File::KeePass-style hashes
  my @all_entries_hashes = ();
  foreach my $ent (@all_entries_flattened) {
    push @all_entries_hashes, entry_as_hash($ent);
  }

  ENT: foreach my $ent (@all_entries_hashes) {
    if (recent_sigint()) { return (); } # Bail on SIGINT
    # If we don't have this entry recorded in all_ent_paths_rev then
    # we can't report on it. The only case known of is when we have
    # multiple entries at the same level (unsupported) and typically
    # that's only seen in /Backup in v1 databases.
    if (! defined($state->{all_ent_paths_rev}->{getID($ent)})) {
      next ENT;
    }
    # Now test the expired time...
    if (does_expire_never($kdb_ver, $ent)) { next ENT; }
    my $exp = $ent->{expires};
    my $title = getLabel($ent);
    if ($exp !~ m/^(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})$/) {
      print "Warning: Invalid expiration date found in \"$title\"\n";
      next ENT;
    }
    my ($year,$mon,$mday,$hour,$min,$sec) = ($1, $2, $3, $4, $5, $6);
    my $timegm = timegm($sec,$min,$hour,$mday,$mon-1,$year);
    if ($timegm < time) {
      push @expired, $ent;
    }
  }
  return @expired;
}

sub cli_purge($$) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # Users can provide a --no-recycle option and -r for recurse.
  my $target = undef;
  my $purge_group='';
  my %opts=();
  {
    local @ARGV = @{$params->{args}};
    my $result = &GetOptions(\%opts, 'r', 'no-recycle');
    if (scalar(@ARGV) != 1 || length($ARGV[0]) < 1) {
      print "Purge only supports exactly one group at a time.\n";
      return;
    }
    $target = normalize_path_string($ARGV[0]);
    if (defined($state->{all_grp_paths_fwd}->{$target})) {
      my $group_id = $state->{all_grp_paths_fwd}->{$target};
      $purge_group = get_group_by_uuid($state->{kdb}, $group_id);
    } else {
      print "Invalid group.\n";
      return;
    }
  }

  # Collect the date/time field that the user wants to purge by
  print "Purge by (c)reated, (e)xpires, or last (a)ccessed/(m)odified time? ";
  my $purge_by=get_single_key();
  print "\n";
  if ($purge_by !~ m/^[ecam]$/i) {
    print "Operation canceled.\n";
    return;
  }

  # Ask the user for the $purge_qty and $purge_uom
  print "Purge entries order than... (90d, 13w, 6m, 2y, etc)? ";
  my $purge_age = get_single_line();
  print "\n";
  my ($purge_qty, $purge_uom) = (undef, undef);
  if ($purge_age !~ m/^(\d+)([dwmy])$/i) {
    print "Invalid age specified.\n" .
	"\n" .
	"Examples:\n" .
	" - 90d = 90 days\n" .
	" - 13w = 13 weeks\n" .
	" -  6m =  6 months\n" .
	" -  2y =  2 years\n" .
	"\n" .
	"Operation canceled.\n";
    return;
  } else {
    ($purge_qty, $purge_uom) = ($1, $2);
  }
  # Make a $purge_time Time::Piece object for the user's chosen purge time
  my $time_now = Time::Piece->new;
  my $purge_time = undef;
  if ($purge_uom eq 'd') {
    $purge_time = $time_now - ONE_DAY * $purge_qty;
  } elsif ($purge_uom eq 'w') {
    $purge_time = $time_now - 7 * ONE_DAY * $purge_qty;
  } elsif ($purge_uom eq 'm') {
    $purge_time = $time_now->add_months(-1*$purge_qty);
  } elsif ($purge_uom eq 'y') {
    $purge_time = $time_now->add_years(-1*$purge_qty);
  }

  # Gather the @groups and @ents that are purge candidates
  my @groups = ($target);
  if ($opts{'r'}) {
    my @child_grps = grep(/^\Q$target\E\0/,
		sort(keys(%{$state->{all_grp_paths_fwd}})));
    foreach my $grp (@child_grps) {
      push @groups, $grp;
    }
  }
  my @ents = ();
  foreach my $grp (@groups) {
    my @ent_paths = grep(/^\Q$grp\E\0[^\0]+$/,
			sort(keys(%{$state->{all_ent_paths_fwd}})));
    foreach my $ent_path (@ent_paths) {
      my $entry_id = $state->{all_ent_paths_fwd}->{$ent_path};
      my $ent = get_entry_by_uuid($state->{kdb}, $entry_id);
      push @ents, $ent;
    }
  }
  # Place the "entries to purge" into @purge_ents
  my %byK = (
        'e' => 'expires', 'c' => 'created',
        'a' => 'accessed', 'm' => 'modified',
        );
  my %byKX = (
        'e' => 'expiry_time', 'c' => 'creation_time',
        'a' => 'last_access_time', 'm' => 'last_modification_time',
        );
  my @purge_ents = ();
  foreach my $ent (@ents) {
    my $ent_time = undef;
    if (ref($state->{kdb}) eq 'File::KeePass') {
      $ent_time = $ent->{$byK{$purge_by}}; # %Y-%m-%d %H:%M:%S
      $ent_time =~ s/[^0-9]//g;
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      my $method = $byKX{$purge_by};
      $ent_time = $ent->$method();  # Mon Jul 18 18:35:35 2022
      $ent_time = Time::Piece->strptime($ent_time, "%a %b %d %T %Y");
      $ent_time = $ent_time->strftime("%Y%m%d%H%M%S");
    }
    my $prg_time = $purge_time->strftime("%Y%m%d%H%M%S");
    if ($ent_time =~ m/^\d{14}$/ && $ent_time < $prg_time) {
      push @purge_ents, $ent;
    }
  }

  if (scalar(@purge_ents) < 1) {
    print "No entries match your purge criteria. Nothing to purge.\n";
    return;
  }

  # Show the user the impact this purge will have and request confirmation
  my %byV = (
	'e' => 'expired', 'c' => 'created',
	'a' => 'last accessed', 'm' => 'last modified',
	);
  my %uomV = (
	'd' => 'day(s)', 'w' => 'week(s)',
	'm' => 'month(s)', 'y' => 'year(s)',
	);
  my $recursivelyV='';
  if ($opts{'r'}) { $recursivelyV = "recursively " }
  print "\n";
  print "For group \"".getLabel($purge_group)."\"\n" .
	" - " . $recursivelyV . "purge entries with $byV{$purge_by} dates " .
		"older than $purge_qty $uomV{$purge_uom}.\n" .
	"   - $purge_qty $uomV{$purge_uom} ago is " .
		$purge_time->strftime("%Y-%m-%d at %H:%M:%S") . "\n" .
        " - this will purge " .scalar(@purge_ents). " of " .scalar(@ents) .
		" entries in " .scalar(@groups). " groups.\n";
  if ($opts{'no-recycle'}) {
    print " - and with --no-recycle specified, no backups will be made!\n";
  }
  print "\n";
  print "Confirm if you would you like to do this? [y/N] ";
  my $key=get_single_key(); print "$key\n";
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  if (lc($key) ne 'y') {
    print "Operation canceled.\n";
    return;
  }

  # Delete the entries that we need to purge
  foreach my $ent (@purge_ents) {
    # No recycling for "Backup"/"Recycle Bin" folders.
    # Other folders respect $opts->{no-recycle}.
    my $ent_id = getID($purge_group);
    my $bugrp_id = get_recycle_group_uuid($state, 0);
    if ( (!$opts->{'no-recycle'}) && $ent_id ne $bugrp_id ) {
      my $errmsg = recycle_entry($state, $ent);
      if (defined($errmsg)) { print "WARNING: $errmsg\n"; }
    }
    if (recent_sigint()) { return undef; } # Bail on SIGINT
    if (ref($state->{kdb}) eq 'File::KeePass') {
      $state->{kdb}->delete_entry({ id => getID($ent) });
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      if (! $ent->remove) {
        print "WARNING: failed to remove the entry. Not sure why...\n";
      }
    }
  }

  # If we purged anything, set kdb_has_changed state, ask to save, etc.
  if (scalar(@purge_ents) > 0) {
    $state->{kdb_has_changed}=1;
    refresh_state_all_paths();
    RequestSaveOnDBChange();
  }
}

sub cli_find($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  destroy_found();

  # Users can provide a -a option to search more than just the title. We
  # use GetOpts to parse this command line.
  my $search_str='';
  my %opts=();
  {
    local @ARGV = @{$params->{args}};
    my $result = &GetOptions(\%opts, 'a', 'expired');
    if (defined($opts{'expired'})) {
      if (scalar(@ARGV) || scalar(keys(%opts)) > 1) {
        print "-expired cannot have search criteria or other qualifiers.\n";
        return;
      }
    } else {
      if (scalar(@ARGV) != 1) {
        print "Find only supports searching for one word.\n";
        return;
      }
      $search_str = $ARGV[0];
    }
  }

  my @e = ();
  my $k=$state->{kdb};

  if (length($search_str)) {
    $search_str = decode_if_not_utf8($search_str) if ($ALL_USER_INPUT_TO_UTF8);
    print "Searching for \"$search_str\" ...\n";

    # Make $search_str a case-insensitive regex
    my @letters=split(//, $search_str);
    foreach my $l (@letters) {
      if (uc($l) ne lc($l)) {
        $l='[' . uc($l) . lc($l) . ']';
      }
    }
    $search_str=join('', @letters);

    # Below, we want to skip the Recycle Bin, if it exists
    my $bugrp_id = get_recycle_group_uuid($state, 0);
    my @skip_uuids = ();
    if (defined($bugrp_id)) {
      push @skip_uuids, $bugrp_id;
    }

    my @srch_flds = qw(title); # Default to just the title
    if ($opts{'a'}) {
      @srch_flds = @ALL_FIND_FIELDS;
    }
    foreach my $fld (@srch_flds) {
      my @ents = (); # Holds candidates for one loop cycle "$fld (@srch_flds)"
      if (ref($k) eq 'File::KeePass') {
        my $search_params = { "$fld =~" => $search_str };
        push @ents, $k->find_entries($search_params);
      } elsif (ref($k) eq 'File::KDBX') {
        my $search_params = { $fld => { '=~' => $search_str } };
        #warn "LHHD: File::KDBX search_params=".Dumper($search_params)."\n";
        my $entries = $k->entries->where($search_params);
        @ents = @{$entries->to_array()};
      }

      # Push all @ents on @e that aren't in exclude groups (skip_uuid).
      ENT: foreach my $ent (@ents) {
        my $parent_group = get_parent_group_of_uuid($k, getID($ent));
        foreach my $skip_uuid (@skip_uuids) {
          next ENT if (getID($parent_group) eq $skip_uuid);
        }
        push @e, $ent;
      }
    }
  } elsif (defined($opts{'expired'})) {
    @e = find_expired_entries($state->{kdb_ver}, $k);
  }

  # Unique the entries in @e
  my %uniqer = ();
  foreach my $ent (@e) {
    my $uuid = getID($ent);
    next if (defined($uniqer{$uuid})); # Already seen it
    $uniqer{$uuid} = $ent;
  }
  @e = values %uniqer; # The unique list

  # Remove Meta-Info/SYSTEM entries
  my @non_meta_info = ();
  foreach my $ent (@e) {
    if (! (getLabel($ent) eq 'Meta-Info' && get_username($ent) eq 'SYSTEM')) {
      push @non_meta_info, $ent;
    }
  }
  @e = @non_meta_info;

  if ( scalar(@e) < 1) {
    print "No matches.\n";
    return;
  }

  # If we get this far we have results to add to a new /_found
  my $found_group = addGroup($k,undef,{title => $FOUND_DIR});
  my $found_gid = getID($found_group);
  $state->{found_gid} = $found_gid;

  # Seed %dup_titles
  my %dup_titles=();
  foreach my $ent (@e) {
    my $lbl = getLabel($ent);
    if (! defined($dup_titles{$lbl})) {
      $dup_titles{$lbl} = 0;
    } else {
      $dup_titles{$lbl} = 1; # So we start printing at #1 below.
    }
  }

  $k->unlock;
  my @matches=();
  FINDS: foreach my $ent (@e) {
    my $new_ent = undef;
    if (ref($k) eq 'File::KeePass') {
      $new_ent = clone($ent); # Clone the entity
      $new_ent->{id} = int(rand(1000000000000000)); # A random new id
      $new_ent->{group} = $found_gid; # Place this entry clone into /_found
    } elsif (ref($k) eq 'File::KDBX') {
      # Repull the $ent from get_entry_by_uuid() to populate some stuff
      # that File::KDBX doesn't provide and then clone it.
      $new_ent = get_entry_by_uuid($k, getID($ent))->clone(
		new_uuid => 1, history => 0,
		reference_password => 0, reference_username => 0);
    }

    my $new_ent_title = getLabel($new_ent);
    #warn "LHHD: considering to add /_found ent: $new_ent_title\n";

    # $new_ent->{path} is _NOT_ a normal key for File::KeePass but this is
    # safe because we are adding it to entries in the /_found group which
    # will not be saved to a file.
    my $nulled_path=$state->{all_ent_paths_rev}->{getID($ent)};
    my @path_pieces = split(/\0/, $nulled_path);
    if (scalar(@path_pieces) > 1 && scalar(grep(/^old$/i, @path_pieces))) {
      $new_ent->{'__in_old_dir'} = 1; # Mark as being in an OLD directory (only safe in /_found).
    }
    $new_ent->{full_path} = '/' . humanize_path($nulled_path); # is this File::KDBX safe?
    $new_ent->{path} = dirname($new_ent->{full_path}) . '/';
    # Modify any duplicate titles by adding a count to the each one
    if ($dup_titles{getLabel($new_ent)} > 0) {
      my $orig_lbl = getLabel($new_ent); # Store for incrementing just below
      my $lbl = getLabel($new_ent) .
			sprintf($DUP_ENTRIES_FORMAT, $dup_titles{getLabel($new_ent)});
      setLabel($new_ent, $lbl);
      #print "LHHD-find-dupes(): ".Dumper([$ent, $new_ent])."\n";
      $dup_titles{$orig_lbl}++;
    }
    #warn "LHHD: want to add /_found ent: $new_ent_title\n";
    if (ref($k) eq 'File::KeePass') {
      $k->add_entry($new_ent);
    } elsif (ref($k) eq 'File::KDBX') {
      my $found_group = get_group_by_uuid($k, $found_gid);
      $found_group->add_entry($new_ent);
    }
    push(@matches, $new_ent);
    # If the user hit ^C (SIGINT) then we need to stop
    if (recent_sigint()) {
      # If we delete the $FOUND_DIR group it should be safe to leave
      destroy_found();
      return undef;
    }
  }
  $k->lock;

  # Because we added a new /_found we must refresh our $state paths
  refresh_state_all_paths();

  # We derive the *true* FOUND_PATH from the $found_gid because it
  # differs between File::KeePass and File::KDBX.
  my $nulled_path=$state->{all_grp_paths_rev}->{$found_gid};
  my $found_path = '/' . humanize_path($nulled_path, 0); # No UTF-8 here!
  $state->{found_path} = $nulled_path;
  $state->{found_gid} = $found_gid;

  # Tell the user what we found
  print " - ".scalar(@matches)." matches found and placed into $found_path\n";

  # If we only found one, ask the user if they want to see it
  if (scalar(@matches) == 1) {
    print "Would you like to show this entry? [y/N] ";
    my $key=get_single_key(); print "$key\n";
    if (lc($key) eq 'y') {
      # We first cli_ls() so that things like xN work on the entry
      cli_ls($self,{"args" => [ $found_path ]});
      # Now show the entry
      my $full_path="$found_path/" . getLabel($e[0], 1); # Can't have utf8 here
      my $show_args = [ $full_path ];
      # If we are doing an expired password search, find only one entry,
      # and give the user the option to show it, we want to show the
      # expired time, and so we add -a here.
      if (defined($opts{'expired'})) { push @{$show_args}, '-a'; }
      cli_show($self, { args => $show_args });
    }
  } elsif (scalar(@matches) > 1) {
    print "Would you like to list them now? [y/N] ";
    my $key=get_single_key(); print "$key\n";
    if (lc($key) eq 'y') {
      cli_ls($self,{"args" => [ $found_path ]});
    }
  }
}

# Something is going wrong between KeePassX and File::KeePass related to
# the unknown values read/written by File::KeePass from/to files written
# by KeePassX. Commenting out line 378 of File/KeePass.pm is one fix,
# this prevents me from needing to do that by just removing the unknown
# values before saving. If there is a downside to this on the KeePassX
# side I've not found it yet. I do have an email out to Paul, the author
# of File::KeePass, requesting some assistance in grokking the problem.
#
# NOTE: I thought that this should not be needed for File::KeePass >= 0.3,
#       but on 2011-02-02 I discovered that creating new groups with
#       File::KeePass and not scrubbing on save created corrupt files:
#               "Group header offset is out of range" errors.
#       Sourceforge bug# 3187054 demonstrated the problem as well.
sub scrub_unknown_values_from_all_groups {
  our $state;
  # No need to do this with newer versions of File::KeePass (fixed in 2.01)
  if (version->parse($File::KeePass::VERSION) >= version->parse('2.03')) {
    return;
  }
  my $k=$state->{kdb};
  my @all_groups_flattened = get_all_groups($k); # Every group in the file!
  my @unkown_field_groups=();
  foreach my $g (@all_groups_flattened) {
    if (defined($g->{unknown})) {
      #warn "LHHD: " . &Dumper($g->{unknown}) . "\n";
      delete $g->{unknown};
      push @unkown_field_groups, getLabel($g);
    }
  }
  my $count = scalar(@unkown_field_groups);
  if ($count > 0) {
    warn "Deleted unknown fields from these $count groups: " .
					join(", ", @unkown_field_groups) . "\n";
  }
}

sub deny_if_readonly {
  my $verbose = shift @_ || 1; # 0 for quiet, 2 to prepend a \n
  our %opts;
  if (defined($opts->{readonly}) && int($opts->{readonly})) {
    if ($verbose) {
      if ($verbose == 2) { print "\n"; }
      print "Function not available with --readonly set.\n";
    }
    return 1;
  }
  return 0;
}

sub cli_save($) {
  my $self = shift @_;
  my $params = shift @_;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  our $state;
  if (! length($state->{kdb_file})) {
    print "Please use the saveas command for new files.\n";
    return;
  }

  # Check for a lock file that we did not place there
  my $lock_file = $state->{kdb_file} . '.lock'; # KeePassX style
  if (-f $lock_file && defined($state->{placed_lock_file}) &&
				$state->{placed_lock_file} ne $lock_file) {
    print color('bold yellow') .  "WARNING:" . color('clear') .
        color('red') .
               " A KeePassX-style lock file is in place for this file.\n" .
		"         It may be opened elsewhere. Save anyway? [y/N] " .
        color('clear');
    my $key=get_single_key(); print "$key\n";
    if (lc($key) ne 'y') {
      return;
    }
  }

  # Derive a temporary, savetmp file to write to.
  my $kdb_savetmp = abs_path($state->{kdb_file});
  $kdb_savetmp =~ s/([.]kdb.*)$/-savetmp$1/;
  if ($kdb_savetmp eq abs_path($state->{kdb_file})) {
    $kdb_savetmp = $kdb_savetmp . "-savetmp"; # Should never happen
  }
  unlink($kdb_savetmp) if (-e $kdb_savetmp);
  if (-e $kdb_savetmp) {
    print color('bold red') . "ERROR: " . color('clear') .
	color('red') . "Something exists at path $kdb_savetmp!\n" .
			"\nSave abandoned!\n" . color('clear');
    return -1;
  }

  # If we got this far the user is OK with us locking the file even
  # if we had a contention.
  touch_file($lock_file);
  $state->{placed_lock_file} = $lock_file;

  my $master_pass = undef; # Set below based on File::KeePass or File::KDBX

  # Scrub the data and write the file
  destroy_found(); # Remove any /_found that we may have created
  my $k=$state->{kdb};

  utf8_change_strings_KDBv1($state, 'encode'); # Encode to bytestring
  $k->unlock; # Required for both File::KeePass and File::KDBX
  if (ref($k) eq 'File::KeePass') {
    $master_pass = composite_master_pass('File::KeePass', $state->{get_master_passwd}(),$state->{key_file});

    scrub_unknown_values_from_all_groups(); # TODO - remove later

    # Note: adding the 3rd parameter (header) here was in response to a bug reported
    # on 03/27/2016 via email to me from a person named marco. There is a bug in
    # File::KeePass that will make this save_db() call revert a V2 database to v1 if
    # the filename does not end in kdbx. Passing the header to this call here works
    # around that bug (a failure to store the version in $self->{version}). I'm not
    # changing this on cli_saveas(), else you could not change the DB versions by
    # using that command with different file extensions. I opened a bug report,
    # here: https://rt.cpan.org/Ticket/Display.html?id=113391
    #
    # I also decided to do this only in the case where a user has a V2 file opened
    # and the filename does not end in kdbx, so that the impact of this change is
    # minimized across the user base.
    if ($state->{kdb_file} !~ m/\.kdbx$/i && $state->{kdb}->{header}->{version} == 2) {
      $k->save_db($kdb_savetmp,$master_pass,$state->{kdb}->{header});
    } else {
      $k->save_db($kdb_savetmp,$master_pass);
    }
  } elsif (ref($k) eq 'File::KDBX') {
    $master_pass = composite_master_pass('File::KDBX', $state->{get_master_passwd}(),$state->{key_file});
    $k->dump_file($kdb_savetmp,$master_pass);
  }
  $k->lock; # Lock protected fields back up

  # Validate that the $kdb_savetmp file can be opened
  # (code copied from open_kdb() and slightly modified)
  if (ref($k) eq 'File::KeePass') {
    my @load_db_warns;
    if (! eval { local $SIG{__WARN__} = sub { push @load_db_warns, @_; };
		my $tmp_kdb = File::KeePass->new;
		$tmp_kdb->load_db($kdb_savetmp, $master_pass) }) {
      my $errmsg = "Couldn't load the new database file $kdb_savetmp\n\n" .
		"Error(s) from File::KeePass:\n$@";
      if (scalar(@load_db_warns)) {
        $errmsg .= "\nWarning(s) from File::KeePass:\n";
        my @warns = map {
		my $t = $_;
		$t =~ s/[^[:print:]]+//g;
		$t =~ s/(Found an unknown header type) \((\d+).+$/$1: $2/;
		$t; } @load_db_warns;
        $errmsg .= " - " . join("\n - ", @warns) . "\n";
      }
      print color('bold red') . "ERROR: " . color('clear') .
	color('red') . $errmsg . "\nSave abandoned!\n" . color('clear');
      unlink($kdb_savetmp);
      return -1;
    }
  } elsif (ref($k) eq 'File::KDBX') {
    my $kdb_obj = File::KDBX->new;
    if (! eval { $kdb_obj->load_file($kdb_savetmp, $master_pass); }) {
      my $error = File::KDBX::Error->error($@);
      my $details = $error->details;
      #print Dumper($details)."\n";
      if (defined($error->{error})) {
        print color('bold red') . "ERROR: " . color('clear') .
		color('red') . "Errors from File::KDBX:\n$error->{error}\n".
		"\nSave abandoned!\n" . color('clear');;
      }
    }
  } else {
    # Should be impossible
    warn "Please report bug \"5jwgs9\" in the saveas command...\n";
  }

  # We hold a read file handle open for no reason other than
  # to show up in lsof. Close it prior to saving the database,
  # else Windows has problems (reported in SF patch #11).
  if (defined($state->{kdb_file_handle})) {
    close $state->{kdb_file_handle};
  }

  # Move $kdb_savetmp into its permanent place.
  if (move($kdb_savetmp, $state->{kdb_file})) {
    $state->{kdb_has_changed}=0; # set our state to no change since last save
    $master_pass="\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0";
    print "Saved to $state->{kdb_file}\n";
  } else {
    print color('bold red') . "ERROR: " . color('clear') .
	color('red') .
		"Failed to move $kdb_savetmp to $state->{kdb_file}" .
	color('clear');
    unlink($kdb_savetmp);
  }

  # Reopen file handle to show up in lsof...
  $state->{kdb_file_handle} = new FileHandle;
  open($state->{kdb_file_handle}, '<', $state->{kdb_file});

  # Update the md5sum of the file after we just saved it
  $state->{kdb_file_md5} = Digest::file::digest_file_hex($state->{kdb_file}, "MD5");

  # Now handle any autosave entries that this database may have
  handle_autosaves();
}

sub handle_autosaves() {
  our $state;

  my $k=$state->{kdb};
  my $autosaves_group=undef;
  my @ents = ();
  if (ref($k) eq 'File::KeePass') {
    $autosaves_group = $k->find_group({level=>0,title=>$AUTOSAVES_DIR});
    if (defined($autosaves_group)) {
      @ents = $k->find_entries({group_id => getID($autosaves_group)});
    }
  } elsif (ref($k) eq 'File::KDBX') {
    my $root_groups = $state->{kdb}->root->groups();
    ROOT_GROUPS: foreach my $grp (@{$root_groups}) {
      if ($grp->name eq $AUTOSAVES_DIR) {
        $autosaves_group=$grp;
        last ROOT_GROUPS;
      }
    }
    if (defined($autosaves_group)) {
      foreach my $ent (@{ $autosaves_group->entries }) {
        push @ents, get_entry_by_uuid($k, getID($ent));
      }
    }
  }

  if (scalar(@ents) < 1) {
    print "No autosaves are defined...\n";
    return 0;
  } else {
    print "Defined autosaves:\n";
    print join("\n", @{get_human_entry_list(\@ents, 1)}) . "\n";
    print color('red')."Process these autosaves? [y/N]: ".color('clear');
    my $key=get_single_key(); print "$key\n";
    if (lc($key) ne 'y') {
      return;
    }

    # If we are here we have autosaves to process.

    destroy_found();  # Remove /_found dir if it exists

    # Process each one.
    foreach my $ent (@ents) {
      my $as_file = $ent->{url};
      $as_file = dirname($state->{kdb_file}) . "/" . $as_file;
      my $as_file_lock = $as_file . ".lock";
      if (-e $as_file_lock) {
        print color('yellow') .
		"Skipped \"".getLabel($ent)."\" due lock file." .color('clear')."\n";
      }

      {
        # Evaluate and warn about problematic autosave file extensions
        my ($asfile_ext) = $as_file =~ m/^.+[.]([^.]+)$/;
        my ($myfile_ext) = $state->{kdb_file} =~ m/^.+[.]([^.]+)$/;
        $asfile_ext = lc($asfile_ext);
        $myfile_ext = lc($myfile_ext);
        my $bnf = basename($as_file);
        if ( !defined($asfile_ext) || $asfile_ext !~ m/^kdbx?$/ ) {
          print color('yellow') .
		"WARNING ($bnf): KeePass files should have *.kdb or *.kdbx extensions.".color('clear')."\n";
        } elsif ($asfile_ext ne $myfile_ext) {
          print color('yellow') .
		"WARNING ($bnf): File extension mismatch: source=*.$myfile_ext vs autosave=*.$asfile_ext.".color('clear')."\n";
        }

        # Compare the kdb_ver/kdbx_ver to the autosave's file extension
        my $ftype = undef;
        if (defined($state->{kdbx_ver})) {
          $ftype = $state->{kdbx_ver};
        } elsif ($state->{kdb_ver}) {
          $ftype = $state->{kdb_ver};
        }
        #print "$ftype vs. $asfile_ext\n";
        if (defined($ftype)) {
          if ($ftype == 1 && $asfile_ext ne 'kdb') {
            print color('yellow') .
		"WARNING: Trying to autosave a v$ftype KDB file as a *.$asfile_ext file.".color('clear')."\n";
          } elsif (($ftype == 3 || $ftype == 4) && $asfile_ext ne 'kdbx') {
            print color('yellow') .
		"WARNING: Trying to autosave a v$ftype KDBX file as a *.$asfile_ext file.".color('clear')."\n";
          }
        }
      }

      if (ref($state->{kdb}) eq 'File::KeePass') {
        $state->{kdb}->unlock;
        if ($state->{kdb_file} !~ m/\.kdbx$/i &&
				$state->{kdb}->{header}->{version} == 2) {
          $k->save_db($as_file,$ent->{password},$state->{kdb}->{header});
        } elsif (! $NO_UTF8) {
          # If not in NO_UTF8 mode, en/decode KDBv1 files from/to UTF8 strings,
          # before and after calling $k->save_db().
          utf8_change_strings_KDBv1($state, 'encode'); # Encode to bytestrings
          $state->{kdb}->unlock; # utf8_change_strings_KDBv1() locks the db
          $k->save_db($as_file,$ent->{password});
          utf8_change_strings_KDBv1($state, 'decode'); # Decode to utf8
        } else {
          $k->save_db($as_file,$ent->{password});
        }
        $state->{kdb}->lock;
      } elsif (ref($state->{kdb}) eq 'File::KDBX') {
        my $guard = $state->{kdb}->unlock_scoped;
        $state->{kdb}->dump_file($as_file,$ent->{password});
      } else {
        print "Please report this bug in the autosave command!\n";
        return -1;
      }
    }
    print color('red')."done.".color('clear')."\n";
  }
}

# This subroutine handles the clipboard commands (xw, xu, xp, and xx)
sub cli_xN($$) {
  my $xNcmd = shift @_;
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # If Clipboard is not avaiable we can't do this for the user
  if  (! is_loaded('Clipboard')) {
    print "Error: $xNcmd requires the Clipboard and Capture::Tiny modules:\n" .
	" - https://metacpan.org/pod/Clipboard\n" .
	" - https://metacpan.org/pod/Capture::Tiny\n" .
	"";
    if (defined($state->{OPTIONAL_PM}->{'Clipboard'}->{error})) {
      print "\nThere was an error loading the Clipboard module, as follows:\n" .
		$state->{OPTIONAL_PM}->{'Clipboard'}->{error} . "\n";
    }
    return;
  }

  # Check the version of Clipboard if we're on macOS Catalina or newer.
  # See https://sourceforge.net/p/kpcli/bugs/41/
  if (lc($OSNAME) eq 'darwin') {
    my $osver = get_macos_version();
    if (defined($osver) && defined($osver->{'ProductVersion'})) {
      my $macOSverMax = '10.15.0'; # macOS Catalina began at 10.15.0
      my $ClipVerMin = '0.21';     # Catalina first supported in 0.21
      my $vernum = $osver->{'ProductVersion'};
      if (version->parse($vernum) >= version->parse($macOSverMax)) {
        no strict 'refs';
        my $vstr="Clipboard::VERSION";
        my $Clipboard_ver = ${$vstr};
        if (version->parse($Clipboard_ver) < version->parse($ClipVerMin)) {
          print color('yellow')."WARNING: For macOS $macOSverMax and higher, ".
                "Clipboard $ClipVerMin or newer is needed\n" .color('clear');
        }
      }
    }
  }

  # If we're clearing the clipboard, just do that and return immediately.
  if ($xNcmd eq 'xx') {
    my_clipboard_copy('');
    print "Clipboard cleared.\n";
    return;
  }

  # Find the entry that the user wants to copy to the clipboard from.
  my $target = $params->{args}->[0];
  my $ent=find_target_entry_by_number_or_path($target);
  if (! defined($ent)) {
    print no_entry_at_path_msg($target);
    return -1;
  }

  # 2FA-TOTP generation
  my $otp = undef;
  if ($xNcmd eq 'xo') {
    my ($key2FA,$digest) = get_otp_data($ent);
    if (defined($key2FA) && defined($digest)) {
      $otp = get_totp($key2FA,$digest);
    } else {
      print "No OTP for this entry.\n";
      return -1;
    }
  }

  # Switch over the xN commands and place the data into $to_copy
  my $to_copy = '';
  SWITCH: {
    $xNcmd eq 'xu' && do { $to_copy = $ent->{username}; last SWITCH; };
    $xNcmd eq 'xw' && do { $to_copy = $ent->{url}; last SWITCH; };
    $xNcmd =~ m/^xpx?$/ && do {
			$to_copy = get_password($state->{kdb},$ent);
			last SWITCH; };
    $xNcmd eq 'xo' && do { $to_copy = $otp; last SWITCH; };
    warn "Error: cli_xN() does not know how to handle the $xNcmd command.";
    $to_copy = undef;
  }

  # Copy to the clipboard and tell the user what we did.
  my $cp_map = {
	'xu' => 'username',
	'xw' => 'url',
	'xp' => 'password',
	'xpx' => 'password',
	'xo' => 'OTP',
	};
  if (defined($to_copy)) {
    my_clipboard_copy($to_copy);
    print "Copied $cp_map->{$xNcmd} for \"".getLabel($ent)."\" to the clipboard.\n";
  }

  # The user has asked us to auto-clear the clipboard
  my $xpxsecs = $opts->{xpxsecs} - 1;
  if ($xNcmd eq 'xpx') {
    for my $n (reverse (0..$xpxsecs)) {
      for my $i (reverse (0..9)) {
        if (($i > 0 || $n == 0) && !($i % 3)) {
          print "\rClipboard will be cleared in $n.$i seconds...";
        }
        if (recent_sigint()) { print "\n"; return undef; } # Bail on SIGINT
        Time::HiRes::sleep(0.1);
      }
    }
    print "\n";
    my_clipboard_copy('');
    print "Clipboard cleared.\n";
    return;
  }

  return;
}

sub my_clipboard_copy($) {
  my $text_to_copy = shift @_;
  # X11 has multiple clipboards and we allow users control over which
  # one(s) to copy to. Without --xclipsel set, Clipboard::Xclip->copy()
  # defaults to primary (the middle mouse click clipboard).
  if ($Clipboard::driver eq 'Clipboard::Xclip' && length($opts->{xclipsel})) {
    if ($opts->{xclipsel} eq 'all') {
      # Clipboard v0.19 (2019-01-31) and newer have copy_to_all_selections()
      # but prior do not. Prior versions are still commonly in use, and
      # so I chose to support them. At a later date, the else statement
      # here could be removed and we could instead insist on a newer
      # version of Clipboard. TODO
      if (Clipboard->can('copy_to_all_selections')) {
        Clipboard->copy_to_all_selections($text_to_copy);
      } else {
        my @x11_sels = $Clipboard::driver->all_selections();
        foreach my $sel (@x11_sels) {
          $Clipboard::driver->copy_to_selection($sel, $text_to_copy);
        }
      }
    } else {
      # Clipboard has no copy_to_selection(), but Clipboard::Xclip does
      $Clipboard::driver->copy_to_selection($opts->{xclipsel}, $text_to_copy);
    }
  } else {
    Clipboard->copy($text_to_copy);
  }
}

sub cli_rm($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $target = $params->{args}->[0];
  my $ent=find_target_entry_by_number_or_path($target);
  if (! defined($ent)) {
    print no_entry_at_path_msg($target);
    return -1;
  }

  # Recycle the entry unless --no-recycle
  if (! (defined($opts->{'no-recycle'}) && int($opts->{'no-recycle'}))) {
    my $errmsg = recycle_entry($state, $ent);
    if (defined($errmsg)) { print "WARNING: $errmsg\n"; }
  }

  # Remove the entry
  if (ref($state->{kdb}) eq 'File::KeePass') {
    $state->{kdb}->delete_entry({ id => getID($ent) });
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    # For File::KDBX, the recycle_entry() routine can accomplish 100% of
    # the work needed and so the entry may already be gone by way of
    # being moved to the Recycle Bin. If that's the case, there is nothing
    # else for us to do. If the entry is still in place, remove it.
    my $ent=find_target_entry_by_number_or_path($target);
    if (defined($ent) && (! $ent->remove)) {
      print "WARNING: failed to remove the entry. Not sure why...\n";
    }
  }

  $state->{kdb_has_changed}=1;
  refresh_state_all_paths();
  RequestSaveOnDBChange();
}

# This routine takes one parameter that will be either a path
# to an entity or an entity number as shown by the ls command
# and will use $state information such as last_ls_ents to
# return a reference to that entity in the $state->{kdb} database,
# if possible (valid input).
sub find_target_entry_by_number_or_path($) {
  my $target=shift @_;
  our $state;

  my $ent=undef; # hope to populate this in a second...

  # This section looks for an entity by an "ls" number
  if ($target =~ m/^[0-9]+$/ && scalar(@{$state->{last_ls_ents}}) > 0
			&& $target < scalar(@{$state->{last_ls_ents}}) ) {
    return @{$state->{last_ls_ents}}[$target];
  }

  # This section looks by a path name
  if (defined $state->{all_ent_paths_fwd}->{normalize_path_string($target)}) {
    my $entry_id=$state->{all_ent_paths_fwd}->{normalize_path_string($target)};
    $ent = get_entry_by_uuid($state->{kdb}, $entry_id);
  }

# NOTE: on 04/12/2024, Lester removed this code because it seems that it was
# misguided from the start. The only time that $ent->{path} should be added
# is by the find command and that is only so that showing entries in the found
# folder shows the user where they actually live. No idea what I was thinking
# when I added this code, but it actually creates a bug on mv, and so it's axed.
#  # If we found the entry, place the path to this entry in the entry record,
#  # even if it's already there (it may have just changed via cli_mv), if the
#  # path we have for this entity is not the $FOUND_DIR.
#  if (defined($ent)) {
#    my $ent_in_FOUND = 0;
#    if (defined($state->{found_gid})) { # A $FOUND_DIR exists
#      my $parent_group = get_parent_group_of_uuid($state->{kdb}, getID($ent));
#      if (getID($parent_group) eq $state->{found_gid}) { # parent == FOUND_DIR
#        $ent_in_FOUND = 1;
#      }
#    }
#    if (! $ent_in_FOUND) {
#      my $full_path = '/' .
#		humanize_path($state->{all_ent_paths_rev}->{getID($ent)});
#      my $path = dirname($full_path) . '/';
#      $ent->{full_path} = $full_path;
#      $ent->{path} = $path;
#    }
#  }

  return $ent;
}

sub cli_rename($$) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $target_dir = $params->{args}->[0];
  my $dir_normalized=normalize_path_string($target_dir);
  my $grp=undef;
  if (defined($state->{all_grp_paths_fwd}->{$dir_normalized})) {
    my $grp_id = $state->{all_grp_paths_fwd}->{$dir_normalized};
    $grp = get_group_by_uuid($state->{kdb}, $grp_id);
  }
  if (! defined($grp)) {
    print "Unknown group: $target_dir\n";
    return -1;
  }

  my $prompt = color('clear')."Enter the group's new Title: ";
  my $term = get_prepped_readline_term();
  my $new_title = $term->readline($prompt);
  my $new_title_not_utf8 = $new_title; # Prior to possible conversion
  $new_title = decode_if_not_utf8($new_title) if ($ALL_USER_INPUT_TO_UTF8);
  # If the user hit ^C (SIGINT) then we need to stop
  if (recent_sigint()) { return undef; }
  chomp($new_title);
  if (length($new_title)) {
    if ($new_title =~ m/\//) {
      print "kpcli cannot support titles with slashes (/) in them.\n";
      return undef;
    }
    # If the titles are the same then there is nothing to do
    my $orig_title = getLabel($grp); # Note, was $grp->name prior.
    if (eq_w_utf8_check($new_title,$orig_title)) { return 0; } # A no-op...
    # Check the new title for same-name conflicts in its group
    my $path = dirname('/'.humanize_path($dir_normalized));
    my $testdir=normalize_path_string("$path/$new_title_not_utf8");
    if (defined($state->{all_grp_paths_fwd}->{$testdir})) {
      print "An entry titled \"$new_title\" is already in $path.\n";
      return undef;
    }
    # If we passed all of our sanity checks then set the new title
    if (ref($state->{kdb}) eq 'File::KeePass') {
      $grp->{title} = $new_title; # This ->{title} is OK!
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      $grp->label($new_title);
    }
  } else {
    return 0;
  }

  # Because we renamed a group we must refresh our $state paths
  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();
}

sub cli_mv {
  my $self = shift @_;
  my $params = shift @_;
  my $src_path = shift @_;
  my $target_dir = shift @_;
  my $skip_save = shift @_ || 0;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  # The target has to be a group. We start validation there (the target).
  my $dir_normalized=normalize_path_string($target_dir);
  my $grp=undef;
  if (defined($state->{all_grp_paths_fwd}->{$dir_normalized})) {
    my $grp_id = $state->{all_grp_paths_fwd}->{$dir_normalized};
    $grp = get_group_by_uuid($state->{kdb}, $grp_id);
  }
  if (! defined($grp)) {
    print "Unknown group: $target_dir\n";
    return -1;
  }

  # The source (thing we are moving) can be an entity, group, or a
  # shell_expansion. Here we figure out which one and prepare to
  # exectute the move(s) below.
  my $ent=undef;
  my $mv_type = undef;
  if ($ent=find_target_entry_by_number_or_path($src_path)) {
    $mv_type = 'entry';
  } elsif (defined($state->{all_grp_paths_fwd}->{normalize_path_string($src_path)})) {
    $mv_type = 'group';
  } else {
    # For shell_expansion moves, we call cli_mv for each shell_expansion item,
    # with skip_save set to true.
    my @ent_matches = shell_expansion($src_path);
    if (scalar(@ent_matches) > 0) {
      $mv_type = 'shell_expansion';
      foreach my $mv_src (@ent_matches) {
        my $skip_save = 1;
        cli_mv($self,$params,'/'.humanize_path($mv_src),$target_dir,$skip_save);
      }
    }
  }
  if (! defined($mv_type)) {
    print "Unknown entity: " . humanize_path($src_path) . "\n";
    return -1;
  }

  # Execute the move of the entry or group.
  if ($mv_type eq 'entry') {
    # Verify no entry title conflict at the new location
    my $new_entry_path=normalize_path_string($target_dir ."/". getLabel($ent));
    if (defined($state->{all_ent_paths_fwd}->{$new_entry_path}) ||
		defined($state->{all_grp_paths_fwd}->{$new_entry_path})) {
      my $path = dirname(humanize_path($new_entry_path));
      print "ERROR: already an item named \"".getLabel($ent)."\" at $path/.\n";
      return undef;
    }

    if (ref($state->{kdb}) eq 'File::KeePass') {
      # Unlock the kdb, clone the entry, remove its ID and set its new group,
      # add it to the kdb, delete the old entry, then lock the kdb...
      $state->{kdb}->unlock;
      my %ent_copy = %{clone($ent)}; # Clone the entity
      delete $ent_copy{id};
      $ent_copy{group} = $grp;
      if ($state->{kdb}->add_entry(\%ent_copy)) {
        $state->{kdb}->delete_entry({ id => getID($ent) });
      }
      $state->{kdb}->lock;
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      $ent->group($grp); # Just set the ent's group to the new $grp
    }

    print 'Moved "'.getLabel($ent).'" to '.dirname(humanize_path($new_entry_path))."/\n";
  } elsif ($mv_type eq 'group') {
    # Find the group that the user is asking us to move
    my $src_grp_uuid = $state->{all_grp_paths_fwd}->{normalize_path_string($src_path)};
    my $src_grp = get_group_by_uuid($state->{kdb}, $src_grp_uuid);
    my $grp_title = getLabel($src_grp);
    my $new_group_path=normalize_path_string($target_dir ."/". $grp_title);
    if (defined($state->{all_grp_paths_fwd}->{$new_group_path}) ||
		defined($state->{all_ent_paths_fwd}->{$new_group_path})) {
      my $path = dirname(humanize_path($new_group_path));
      print "ERROR: already an item named \"$grp_title\" at $path/.\n";
      return undef;
    }

    if (ref($state->{kdb}) eq 'File::KeePass') {
      # Clone the group that is to be moved
      my %new_group = %{$src_grp};
      # Delete the id and level from the cloned group
      delete $new_group{id};
      # Add the group ID of the parent we want to put our clone under
      $new_group{group} = getID($grp); # Set the new parent group
      addGroup($state->{kdb},$new_group{group},\%new_group);
      # Delete the original group that we just cloned into a new spot
      $state->{kdb}->delete_group({ id => getID($src_grp) });
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      $src_grp->group($grp); # Just set the src_grp's group to the new $grp
    }

    print "Moved \"$grp_title/\" to ".dirname(humanize_path($new_group_path))."/\n";
  } elsif ($mv_type ne 'shell_expansion') {
    print "Unknown error with move command.\n";
    return -1;
  }

  # Because we moved an entry we must refresh our $state paths
  if (! $skip_save) {
    refresh_state_all_paths();
    $state->{kdb_has_changed}=1;
    RequestSaveOnDBChange();
  }
}

sub cli_copy {
  my $self = shift @_;
  my $params = shift @_;
  my $src = shift @_;
  my $dst = shift @_;
  my $skip_save = shift @_ || 0;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $source_ent = $src;
  my $src_ent=find_target_entry_by_number_or_path($source_ent);
  if (! defined($src_ent)) {
    print "Unknown entry: $source_ent\n";
    return -1;
  }

  my $target_ent = $dst;
  my $trg_ent=find_target_entry_by_number_or_path($target_ent);
  if (defined($trg_ent)) {
    print "Copy cannot overwrite an existing entry.\n";
    return -1;
  }

  # Unlock the kdb, clone the entry, remove its ID and set its new group,
  # add it to the kdb, delete the old entry, then lock the kdb...
  my $ent_copy = undef;
  $state->{kdb}->unlock;
  if (ref($state->{kdb}) eq 'File::KeePass') {
    $ent_copy = clone($src_ent); # Clone the entity
    delete $ent_copy->{id}; # Remove the entry ID for the new copy
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    $ent_copy = $src_ent->clone( new_uuid => 1, history => 0, parent => 1,
		reference_password => 0, reference_username => 0);
  }
  $state->{kdb}->lock;

  my $new_grp_id = undef;
  my $target_path = normalize_path_string($target_ent);
  if (defined($state->{all_grp_paths_fwd}->{$target_path})) {
    # Copying to a group: > copy ./foo_entry ./bar/
    $new_grp_id = $state->{all_grp_paths_fwd}->{$target_path};
  } else {
    # Copying to a entry: > copy ./foo_entry ./bar/bar_entry
    my ($grp_path,$name)=normalize_and_split_raw_path($target_ent);
    # The $name that we have here came directly from the user's command line,
    # from Term::ShellUI, and as such it is not utf8, and it needs to be.
    $name = decode_if_not_utf8(humanize_path($name));
    setLabel($ent_copy, $name);
    # Group needs to be set to the group we may be moving the copy to
    $new_grp_id = $state->{all_grp_paths_fwd}->{$grp_path};
  }
  if (! defined($new_grp_id)) {
    print "Copy failed due to missing target group ID.\n";
    return -1;
  } else {
    setGroup($ent_copy, $new_grp_id);
  }
  if (ref($state->{kdb}) eq 'File::KeePass') {
    # Not sure why these key deletions were done, but there was
    # almost certainly a reason so I am leaving it in place.
    my @flds = qw(accessed auto_type binary comment created expires
	icon modified title password url username id group
	binary auto_type expires_enabled location_changed
	usage_count tags background_color foreground_color
	custom_icon_uuid override_url
	auto_type_enabled auto_type_munge protected strings);
    foreach my $k (keys %{$ent_copy}) {
      delete $ent_copy->{$k} if (!grep(/^$k$/, @flds));
    }

    # print "LHHD: " . Dumper(ref($state->{kdb}),$src_ent,$ent_copy)."\n";
    $state->{kdb}->unlock;
    if (! $state->{kdb}->add_entry($ent_copy)) {
      print "Copy failed on add_entry().\n";
      $state->{kdb}->lock;
      return -1;
    }
    $state->{kdb}->lock;
  }

  # Because we added an entry we must refresh our $state paths
  if (! $skip_save) {
    refresh_state_all_paths();
    $state->{kdb_has_changed}=1;
    RequestSaveOnDBChange();
  }
  return 0;
}

sub cli_clone($$) {
  my $self = shift @_;
  my $params = shift @_;
  my $src = shift @_;
  my $dst = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $skip_save = 1;
  my $retval_copy = cli_copy($self, $params, $src, $dst, $skip_save);
  if ($retval_copy) {
    return -1;
  }
  refresh_state_all_paths();

  my $target_ent = $params->{args}->[1];
  my $ent=find_target_entry_by_number_or_path($target_ent);
  if (! (defined($ent) && defined(getID($ent)))) {
    print "Copy failed.\n";
    return -1;
  }

  $state->{kdb_has_changed}=1;
  my %changes = ();
  my $retval_edit = _entry_edit_gui($ent, \%changes, $state->{kdb_ver});

  # Apply the user changes, update modify time and prompt to save
  if ($retval_edit == 0) {
    update_entry($state->{kdb}, $ent, \%changes);
    refresh_state_all_paths();
    $state->{kdb_has_changed}=1;
    RequestSaveOnDBChange();
    return 0;
  } else {
    # If the edit failed (or if the user hit ^C while in edit_gui), then
    # remove the target entity that cli_copy() made.
    if (ref($state->{kdb}) eq 'File::KeePass') {
      my $ent_id = getID($ent);
      $state->{kdb}->delete_entry({ id => $ent_id });
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      if (! $ent->remove) {
        print "WARNING: failed to remove the entry. Not sure why...\n";
      }
    }
    refresh_state_all_paths();
    $state->{kdb_has_changed}=0; # Should be back to how we started
    return $retval_edit;
  }
}

sub cli_otp($$) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  my ($otp_supported, $reason) = have_otp_support();
  if (! $otp_supported) {
    print color('bold yellow') . $reason . color('clear') . "\n";
    return -1;
  }

  my $target = $params->{args}->[0];
  my $ent=find_target_entry_by_number_or_path($target);
  if (! defined($ent)) {
    return -1;
  }

  # 2FA-TOTP generation
  my ($key2FA,$digest) = get_otp_data($ent);
  if (defined($key2FA) && defined($digest)) {
    my $otp = get_totp($key2FA,$digest);
    print "$otp\n";
    return 0;
  }

  print "No OTP for this entry.\n";
  return -1;
}

# get/set commands
sub get_set_fields_map {
  my $h = {
	title    => 'Title',
	username => 'Uname',
	password => 'Pass',
	url      => 'URL',
	comment  => 'Notes',
	id       => 'ID',
	otp      => 'OTP',
	};
  my $rh = {};
  foreach my $k (keys %{$h}) {
    $rh->{$h->{$k}} = $k;
  }
  return ($h,$rh);
}
sub complete_get_set_fields {
  my $self = shift;
  my $cmpl = shift;
  my ($flds,$rflds) = get_set_fields_map();
  my @completions = sort(uniq((keys %{$flds}, keys %{$rflds})));
  my $path = $cmpl->{tokens}->[$cmpl->{tokno}];
  @completions = grep(/^$path/, @completions);
  return \@completions;
}
sub cli_get($$) {
  my $self = shift @_;
  my $params = shift @_;
  return(getter_setter($self, 'get', $params));
}
sub cli_set($$) {
  my $self = shift @_;
  my $params = shift @_;
  return(getter_setter($self, 'set', $params));
}
sub getter_setter($$$) {
  my $self = shift @_;
  my $action = shift @_;
  my $params = shift @_;
  our $state;
  our $opts;

  my ($target, $field, $newval) = @{$params->{args}};

  # Validate and resolve the field
  my ($flds,$rflds) = get_set_fields_map();
  if (! defined($field)) {
    print "Invalid field name.\n";
    return -1;
  }
  # Map any "human" field names to the proper hash keys
  if (defined($rflds->{$field})) { $field = $rflds->{$field}; }
  if (! defined($flds->{$field})) {
    print "Invalid field name.\n";
    return -1;
  }

  my $ent = find_target_entry_by_number_or_path($target);
  if (! defined($ent)) {
    print "Invalid entry path.\n";
    return -1;
  }

  my $lc_field = lc($field);
  if ($action eq 'get') {
    # Convert $ent to a simple, File::KeePass-style hash for the code below
    $state->{kdb}->unlock; # Because the user can request the password
    my $ent_hash = entry_as_hash($ent);
    $state->{kdb}->lock;
    my $val = $ent_hash->{$field} // undef;
    $val = $ent_hash->{strings}->{$field} // undef if (!defined($val));
    return 0 if (!defined($val)); # Bail out now if we have no $val
    if ($lc_field eq 'id') {
      $val = my_format_uuid($val, '-');
    }
    # The password field is never handed to us utf8 encoded, by any
    # of the modules or formats, and so we decode it here.
    if ($lc_field eq 'password') {
      $val = decode_if_not_utf8($val);
    }
    print "$val\n" if defined($val);
    return 0;
  } elsif ($action eq 'set') {
    if (! defined($newval)) {
      print "You must provide a new value to set for the field.\n";
      return -1;
    }
    if (grep(/^$lc_field$/, qw(id))) {
      print "You cannot set the entrys's ID (UUID).\n";
      return -1;
    }
    # Start by making the $newval UTF-8 and then we'll figure out if
    # we need to make an exception, which is really just password.
    $newval = decode_if_not_utf8($newval);
    my $encode_if_utf8 = 0;
    $encode_if_utf8 = 1 if (lc($lc_field) eq 'password');
    $newval = encode_if_utf8($newval) if ($encode_if_utf8);
    my %changes = ( $field => $newval ); # Just one change
    update_entry($state->{kdb}, $ent, \%changes);
    refresh_state_all_paths();
    $state->{kdb_has_changed}=1;
  } else {
    print "BUG in how getter_setter() was called! Please report.\n";
  }

  return undef;
}
sub get_history {
  my $ent = shift @_;
  if (ref($ent) =~ m/^File::KDBX::/) {
    return $ent->history;
  }
  if (ref($ent) eq 'HASH' and exists($ent->{history})) {
    return $ent->{history};
  }
  return undef;
}
sub get_password {
  my $kdb = shift @_;
  my $ent = shift @_;
  if (ref($kdb) eq 'File::KeePass') {
    my $password = $state->{kdb}->locked_entry_password($ent);
    return $password;
  }
  if (ref($kdb) eq 'File::KDBX') {
    # NOTE: ->peek() fails (returns undef) if the entry is
    # already unlocked, which is why the shenanigans here...
    my $password = $ent->password; # In case it's unlocked.
    if (! defined($password)) {
      # Peek allows decryption of a specific encrypted field,
      # of which only Password is by default.
      $password = $kdb->peek($ent->string('Password'));
    }
    return $password;
  }
  return undef;
}
sub get_username {
  my $ent = shift @_;
  return getk($ent,'username');
}
sub getk {
  my $ent = shift @_;
  my $key = shift @_;
  # These first two cases are the quick/easy ones
  if (ref($ent) =~ m/^File::KDBX::/ && $ent->can($key)) {
    # TODO - may need to investigate protection and ->peek here
    return $ent->$key;
  }
  if (ref($ent) eq 'HASH' and exists($ent->{$key})) {
    return $ent->{$key};
  }

  # If we got this far, then try to run through entry_as_hash()
  my $enth = entry_as_hash($ent);
  if (ref($enth) eq 'HASH' and exists($enth->{$key})) {
    return $enth->{$key};
  }

  warn "WARNING: getk(\$ent,'$key') failed to find a value!\n";
  return undef;
}
# END: get/set commands

# To eliminate a ton of code like this:
# $id = $ent->{id} // $ent->uuid;
sub getID {
  my $obj = shift @_;
  my $printable = shift @_ // 0; # Make it printable?
  if (ref($obj) =~ m/^File::KDBX::/) {
    my $uuid = $obj->uuid; # A binary mess... :)
    $uuid = my_format_uuid($uuid,'-') if ($printable);
    return $uuid;
  }
  if (defined($obj->{id})) { # File::KeePass
    # IDs in File::KeePass are just ints (at least in v1)
    return $obj->{id};
  }
  warn "getID() failed on obj type: ".ref($obj)."\n".
		Dumper($obj)."\n"; # Intentional Dumper
  return undef;
}
# Get an entry or group object by its UUID
sub getObjByID {
  my $uuid = shift @_;
  my $kdb = $state->{kdb};
  if (ref($kdb) eq 'File::KDBX') {
    my $this_objs_itter = $kdb->objects->where( uuid => { 'eq' => $uuid, });
    # Should have exactly one result (uuid=$uuid)
    my $count = $this_objs_itter->size;
    if ($count < 1) {
      warn "WARN: getObjByID() has zero results from File::KDBX!\n";
      return undef;
    } elsif ($count > 1) {
      warn "ERROR/BUG: getObjByID() has more than one result!\n";
    }
    my $this_obj = <$this_objs_itter>;
    return $this_obj;
  } elsif (ref($kdb) eq 'File::KeePass') {
    my $this_obj = $kdb->find_entry( {id=>$uuid} );
    if (! defined($this_obj)) {
      $this_obj = $kdb->find_group( {id=>$uuid} );
    }
    if (defined($this_obj)) {
      return $this_obj;
    }
    warn "WARN: getObjByID() has zero results from File::KeePass!\n";
  } else {
    warn "getObjByID() can't handle \$kdb it was given!\n";
  }
  return undef;
}
# Get an entry's or group's label, from its object or its UUID
sub getLabel {
  my $obj = shift @_;
  my $encode_utf8 = shift @_ // 0; # By default, leave utf8 alone
  my $label = undef;
  # First try by object or hash
  if (ref($obj) =~ m/^File::KDBX::/ && $obj->can("label")) {
    $label = $obj->label;
  }
  if (ref($obj) eq 'HASH' && defined($obj->{title})) { # File::KeePass
    $label = $obj->{title};
  }
  # Maybe we were given a $obj ID, not the $obj itself. If so, pursue that.
  if ((!defined($label)) && ref($obj) eq '' && length($obj) > 0) {
    my $obj_from_id = getObjByID($obj);
    if (defined($obj_from_id)) {
      return getLabel($obj_from_id, $encode_utf8);
    }
  }

  if (! defined($label)) {
    warn "getLabel() failed on obj type: ".ref($obj)."\n";
		#Dumper($obj)."\n"; # Intentional Dumper
    return undef;
  }

  # If we were asked to $encode_utf8 then encode utf8 strings to an octet
  # sequence if the string is currently in utf8 format.  We need to do this
  # sometimes because these labels are used to build and access the non-utf8
  # "normalized path" structures.
  $label = encode_if_utf8($label, 1) if ($encode_utf8);

  return $label;
}
sub setLabel($$) {
  my $obj = shift @_;
  my $str = shift @_;
  #return undef if (!defined($obj));
  if (ref($obj) =~ m/^File::KDBX::/ && $obj->can("label")) {
    $obj->label($str);
    return 0;
  }
  if (defined($obj->{title})) { # File::KeePass
    $obj->{title} = $str;
    return 0;
  }
  warn "setLabel() failed on obj type: ".ref($obj)."\n".
		Dumper($obj,$str)."\n"; # Intentional Dumper
  return undef;
}

# addGroup($kdb,$parent_group_id,{title => 'New Group'});
sub addGroup {
  my $kdb = shift @_ || undef;
  my $parent_grp = shift @_ || undef;
  my $new_grp_info = shift @_ || {};

  #print "LHHDaddg: $new_grp_info->{title}\n";

  if (! (ref($new_grp_info) eq 'HASH' && defined($new_grp_info->{title}))) {
    warn "addGroup() called with invalid \$new_grp_info!\n";
    return undef;
  }
  if (defined($new_grp_info->{group}) &&
				$new_grp_info->{group} ne $parent_grp) {
    warn "addGroup(): conflicting \$parent_grp and \$new_grp_info->{group}!\n";
    return undef;
  }

  my $icon = $new_grp_info->{icon} // $DEFAULT_GROUP_ICON;

  my $new_group = undef;
  if (ref($kdb) eq 'File::KeePass') {
    # File::KeePass method
    $new_group = $kdb->add_group({
        title => $new_grp_info->{title},
        icon => $icon,
        # NOTE: This assumes $parent_grp = UUID. It's also OK for this to be
        # undef for File::KeePass as that just creates a root-level group.
	group => $parent_grp,
    });
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    if (! defined($parent_grp)) {
      # Create a top-level group (under the Root node)
      $new_group = $kdb->add_group(
		name => $new_grp_info->{title}, # name vs title
		icon_id => $icon, # NOTE: icon_id for File::KDBX
		 );
    } else {
      my $parent_group = undef;
      if (ref($parent_grp) eq '') { # not a reference; probably a UUID
        $parent_group = get_group_by_uuid($kdb, $parent_grp);
      } elsif (ref($parent_grp) =~ m/^File::KDBX::Group/) {
        $parent_group = $parent_grp;
      }
      if (defined($parent_group)) {
        $new_group = $parent_group->add_group(
		name => $new_grp_info->{title}, # name vs title
		icon_id => $icon, # NOTE: icon_id for File::KDBX
		 );
      } else {
        warn "addGroup() called with invalid \$parent_grp!\n";
      }
    }
  }

  return $new_group;
}
# This routine sets the group of an entry. It essentially is a move command,
# moving the $obj to the $obj_tgt group.
sub setGroup($$) {
  my $obj = shift @_;
  my $obj_tgt = shift @_;

  # File::KDBX
  if (ref($obj) =~ m/^File::KDBX::/) {
    if (ref($obj_tgt) eq '') { # not a reference; probably a UUID
      my $tgt_grp = get_group_by_uuid($state->{kdb}, $obj_tgt);
      $obj->group($tgt_grp);
      return 0;
    } elsif (ref($obj_tgt) =~ m/^File::KDBX::Group/) {
      $obj->group($obj_tgt);
      return 0;
    }
  }

  # File::KeePass
  if (ref($obj) eq 'HASH' && ref($state->{kdb}) eq 'File::KeePass') {
    if (ref($obj_tgt) eq '') { # not a reference; probably a UUID
      $obj->{group} = $obj_tgt;
      return 0;
    } elsif (defined(getID($obj_tgt))) {
      $obj->{group} = getID($obj_tgt);
      return 0;
    }
  }

  warn "setGroup() failed on obj types:\n".
	Dumper(ref($obj),ref($obj_tgt))."\n"; # Intentional Dumper
  return undef;
}

sub cli_show($$) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;
  our $opts;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # Users can provide a -f option to show the password. We use GetOptions
  # to parse this command line, and $target holds that target.
  my $target='';
  my %opts=();
  {
    local @ARGV = @{$params->{args}};
    my $result = &GetOptions(\%opts, 'f', 'a', 'dump');
    if (scalar(@ARGV) != 1) {
      return -1;
    }
    $target = $ARGV[0];
  }

  my $ent = find_target_entry_by_number_or_path($target);
  # warn "LHHD: ent uuid=".Dumper($ent->uuid)."\n";
  if (! defined($ent)) {
    return -1;
  }

  # TODO - consider using entry_as_hash() to allow us to
  # stop shoving KeePass-style keys into File::KDBX objects.

  # Dumper if the user gave the --dump option to show: "show --dump 0"
  if (defined($opts{dump})) {
    my $tmp_ent = $ent;
    # Don't want to see the KDBX4 history in a --dump
    if (ref($ent) =~ m/^File::KDBX::/) {
      my $guard = $state->{kdb}->unlock_scoped; # Else can't get protected strs
      $tmp_ent = $ent->clone( new_uuid => 0, history => 0,
		reference_password => 0, reference_username => 0);
    } elsif (ref($state->{kdb}) eq 'File::KeePass') {
      $state->{kdb}->unlock; # Required for the password field
    }
    my $parent_group = get_parent_group_of_uuid($state->{kdb}, getID($ent));
    my $parent_grp_label = getLabel($parent_group);
    my $to_dump = {
	path_hum => get_path($ent),
	path_raw => $state->{all_ent_paths_rev}->{getID($ent)},
	ent => $tmp_ent,
	parent_grp_label => $parent_grp_label,
	};
    print Dumper($to_dump)."\n"; # Intentional Dumper
    $state->{kdb}->lock if (ref($state->{kdb}) eq 'File::KeePass');
  }

  # File::KeePass will never give utf8 to us but File::KDBX will,
  # but it should be safe to always do this decode_if_not_utf8().
  my $password = get_password($state->{kdb},$ent) // '';
  $password = decode_if_not_utf8($password);
  # Unless -f is specified, we "hide" the password as red-on-red,
  # unless --nopwprint is set, in which case we don't show it.
  if (! defined($opts{f})) {
    $password = colored(['red on_red'], $password);
    if ($opts->{nopwprint}) { $password = undef; }
  }

  # Number of entries in the entry's history
  my $history_count = 0;
  my $history_arr = get_history($ent);
  if (defined($history_arr) && ref($history_arr) eq 'ARRAY') {
    $history_count = scalar(@{$history_arr});
  }

  # 2FA-TOTP generation
  my $otp = undef;
  if (is_loaded('Authen::OATH')) {
    my ($key2FA,$digest) = get_otp_data($ent);
    if (defined($key2FA) && defined($digest)) {
      my ($otp_supported, $reason) = have_otp_support();
      if (! $otp_supported) {
        print color('bold yellow') . $reason . color('clear') . "\n";
      } else {
        $otp = get_totp($key2FA,$digest);
      }
    }
  }
  # Print the entry for the user
  print "\n";
  if (defined($ent->{path})) { # Placed by the find command
    my $ent_path = decode_if_not_utf8($ent->{path});
    print show_format("Path",$ent_path) . "\n";
  }
  # Only show the 2FA key if both -a and -f are given
  my $notes = getk($ent,'comment');
  if (! (defined($opts{a}) && defined($opts{f})) ) {
    my ($key2FA,$digest) = get_otp_data($ent);
    if (defined($key2FA) && length($key2FA)) {
      $notes =~ s/\Q$key2FA\E/<redacted>/g;
    }
  }
  print
	show_format("Title",getLabel($ent)) . "\n" .
	show_format("Uname",get_username($ent)) . "\n" .
	(defined($password) ? show_format("Pass",$password) . "\n" : '') .
	(defined($otp) ? show_format("OTP",$otp) . "\n" : '') .
	show_format("URL",getk($ent,'url')) . "\n" .
	show_format("Notes",$notes) . "\n" .
	($DEBUG ? show_format("ID", getID($ent)) . "\n" : '');
  # Tags were added to KeePass in v2.11 (*.kdbx)
  if (defined($ent->{tags}) && length($ent->{tags})) {
    print show_format("Tags", humanize_entry_tags($ent->{tags})) . "\n";
  }
  # Check for strings and file attachments in this entry.
  # NOTE: File::KeePass calls these strings and binary.
  #       File::KDBX calls these strings and binaries.
  # show_helper_files_strings() ignores whatever is missing,
  # so looping over all three options is correct here.
  foreach my $key (qw(strings binary binaries)) {
    $state->{kdb}->unlock;
    my $tmp_enth = entry_as_hash($ent);
    $state->{kdb}->lock;
    my $attachment = show_helper_files_strings($tmp_enth, \%opts, $key);
    if (length($attachment)) { print $attachment; }
  }
  # If -a was given, tack on those details
  if (defined($opts{a})) {
    print "" . # The "" prevents diagnostics from making an undue warning...
	($history_count>0 ? show_format("Hist#",$history_count) . "\n" : '') .
	show_format("Icon#",getk($ent,'icon')) . "\n" .
	show_format("Creat",getk($ent,'created')) . "\n" .
	show_format("Modif",getk($ent,'modified')) . "\n";
    if (defined($ent->{expires})) {
      my $expires = getk($ent,'expires');
      if (does_expire_never($state->{kdb_ver}, $ent)) {
        $expires = 'Never';
      }
      print show_format("Xpire",$expires) . "\n";
    }
  }
  print "\n";
}

# A helper function to display key/val pairs and file attachments.
# Note that strings (key/val pairs) and multiple attachments per
# entry only exist in KeePass 2.x (kdbx) files, while verions 1.x
# files (kdb) support only a single file attachment per entry.
sub show_helper_files_strings {
  my $ent = shift @_;
  my $opts = shift @_;
  my $key = shift @_;
  my $labels = {
	'strings'  => ['Strgs','String Values'],    # both
	'binary'   => ['Atchm','File Attachments'], # File::KeePass
	'binaries' => ['Atchm','File Attachments'], # File::KDBX
	};
  my %KDBX_str_skips = map { ($_, 1); } qw(UserName Password Title URL Notes);
  my @atts=();

  # As of 01/22/2025, this routine should only ever get simple hashes,
  # made from entry_as_hash($ent).
  if (ref($ent) ne 'HASH') {
    die "BUG: show_helper_files_strings() passed an \$ent of type ".ref($ent);
  }

  if (defined($ent->{$key}) && ref($ent->{$key}) eq 'HASH') {
    ITEM: foreach my $name (sort keys %{$ent->{$key}}) {
      if ($key eq 'binary' || $key eq 'binaries') { # File::KeePass / File::KDBX
        my $val = $ent->{$key}->{$name}; # File::KeePass has scalar here
        if (ref($val) eq 'HASH' && defined($val->{value})) { # File::KDBX
          $val = $val->{value};
        }
        push @atts, "$name (". int(length($val)) ." bytes)";
      } elsif ($key eq 'strings') {
        if (ref($state->{kdb}) eq 'File::KDBX' && $KDBX_str_skips{$name}) {
          next ITEM; # Skip the normal fields that we display
        }
        my $protected = 0;               # Default to not protected
        my $val = $ent->{$key}->{$name}; # File::KeePass has scalar here
        if (defined($ent->{protected}) &&      # File::KeePass v2 DBs
		ref($ent->{protected}) eq 'HASH') {
          $protected = $ent->{protected}->{$name} // 0;
        }
        # Show the value if it is not proteced or -f was provided,
        # else obfuscate it with red-on-red.
        my $nameV = $name; $nameV = "$name*" if ($protected);
        if ((!$protected) || defined($opts->{f})) {
          push @atts, "$nameV = $val";
        } else {
          push @atts, "$nameV = ".colored(['red on_red'],$val);
        }
      }
    }
  }
  my $attachment = '';
  my $label = $labels->{$key}[0];
  if (scalar(@atts) == 0 && defined($opts->{v})) {
    $attachment = "None";
  } elsif (scalar(@atts) == 1) {
    $attachment = $atts[0];
  } elsif (scalar(@atts) > 1) {
    $label = $labels->{$key}[1];
    my @t=();
    foreach my $num (1..scalar(@atts)) {
      push(@t, sprintf("%2d) %s", $num, $atts[$num-1]));
    }
    $attachment = "\n " . join("\n ", @t) . "\n";
  }
  return ($attachment ne '' ? show_format($label,$attachment) . "\n" : '');
}

sub cli_edit {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $target = $params->{args}->[0];
  my $ent=find_target_entry_by_number_or_path($target);
  if (! defined($ent)) {
    print no_entry_at_path_msg($target);
    return -1;
  }
  my $ent_id = getID($ent);

  # Protect users from editing in the $FOUND_DIR.
  if (defined($state->{found_gid})) { # A $FOUND_DIR exists
    my $parent_group = get_parent_group_of_uuid($state->{kdb}, $ent_id);
    if (getID($parent_group) eq $state->{found_gid}) { # parent == FOUND_DIR
      print color('yellow')
	. "That entity is in the temporary /$FOUND_DIR dir.\n"
	. color('clear');
      my $real_path = $ent->{full_path};
      my $real_ent = find_target_entry_by_number_or_path($real_path);
      if (defined($real_ent)) {
        print "Would you rather edit $real_path? [y/N]";
        my $key=get_single_key(); print "$key\n";
        if (lc($key) eq 'y') {
          $ent = $real_ent;
        }
      }
    }
  }

  my %changes = ();
  my $retval = _entry_edit_gui($ent, \%changes, $state->{kdb_ver});

  # If the user made changes, apply them, update modify time and prompt to save
  if ($retval == 0 && scalar(keys(%changes)) > 0) {
    # Recycle the entry unless --no-recycle
    if (! (defined($opts->{'no-recycle'}) && int($opts->{'no-recycle'}))) {
      my $errmsg = recycle_entry($state, $ent);
      if (defined($errmsg)) { print "WARNING: $errmsg\n"; }
    }

    update_entry($state->{kdb}, $ent, \%changes);

    refresh_state_all_paths();
    $state->{kdb_has_changed}=1;
    RequestSaveOnDBChange();
  }

return 0;
}

# Takes an entry and returns a hash in the form of File::KeePass
sub entry_as_hash($) {
  my $ent = shift @_;

  if (ref($ent) eq 'HASH') { # Likely File::KeePass
    # We clone because the caller may unlock/lock around calling us.
    return clone($ent);
  } elsif (ref($ent) =~ m/^File::KDBX::/) {
    my $h = {
	id		=> $ent->uuid,
	title		=> $ent->label,
	icon		=> $ent->icon_id,
	username	=> $ent->username,
	password	=> get_password($ent->kdbx,$ent),
	url		=> $ent->url,
	comment		=> $ent->notes,
	foreground_color => $ent->foreground_color,
	background_color => $ent->background_color,
	#override_url	=> $ent->override_url, # A TODO item in File::KDBX
	auto_type_enabled => $ent->auto_type_enabled,
	auto_type	=> $ent->auto_type_associations,
	auto_type_munge	=> $ent->auto_type_obfuscation,
	accessed	=> $ent->last_access_time,
	created		=> $ent->creation_time,
	modified	=> $ent->last_modification_time,
	location_changed => $ent->location_changed,
	expires		=> $ent->expiry_time,
	expires_enabled	=> $ent->expires,
	usage_count	=> $ent->usage_count,
	tags		=> $ent->tags,
	strings		=> {}, # Populated below
	binary		=> {}, # Populated below
	};

    # Convert from Time::Piece objects to "YYYY-mm-dd HH:MM:SS"
    # NOTE: File::KDBX accepts this format as valid times.
    foreach my $fld (keys %{$h}) {
      if (ref($h->{$fld}) eq 'Time::Piece') {
        my $orig_time = $h->{$fld};
        $h->{$fld} = $orig_time->strftime("%Y-%m-%d %H:%M:%S");
      }
    }

    # Map strings and binaries to flatter File::KeePass style
    my %to_map = (
	strings => $ent->strings,
	binary	=> $ent->binaries,
	);
    foreach my $type (sort keys %to_map) {
      my $data = $to_map{$type};
      if (ref($data) eq 'HASH') {
        foreach my $str (sort keys %{$data}) {
          my $val = $data->{$str}->{value};
          $h->{$type}->{$str} = $val;
          # The File::KeePass style of protected fields storage
          if (exists($data->{$str}->{protect}) && $data->{$str}->{protect}) {
            $h->{protected}->{$str} = 1;
          }
        }
      }
    }

    # Prune the "standard" strings (KDBX4-style) out of the strings
    foreach my $k (qw(Notes Password Title URL UserName)) {
      delete($h->{strings}->{$k}) if (exists($h->{strings}->{$k}));
    }

    return $h;
  } else {
    warn "entry_as_hash() was given input that it cannot handle: ".Dumper($ent)."\n";
    return undef;
  }
}

sub update_entry($$$) {
  my $kdb = shift @_;
  my $ent = shift @_;
  my $change_ref = shift @_;

  return 0 if (scalar(keys(%{$change_ref})) < 1); # Nothing to do

  my %changes = %{$change_ref}; # Should be small so not a big deal...

  # Update the entry's changed fields
  if (ref($kdb) eq 'File::KeePass') {
    if (defined($changes{otp})) {
      warn "Setting field otp is only supported for KDBX4 and File::KDBX.\n";
      delete($changes{otp});
    }
    $kdb->unlock; # Required for the password field
    foreach my $key (keys %changes) { $ent->{$key} = $changes{$key}; }
    $kdb->lock;
    $ent->{modified} = $kdb->now;
  } elsif (ref($kdb) eq 'File::KDBX') {
    my $guard = $kdb->unlock_scoped; # Else can't set protected strs
    my $txn = $ent->begin_work();    # Start an atomic transaction on $ent
    # Tags
    if (defined($changes{tags})) {
      $ent->tags($changes{tags});
      delete $changes{tags};
    }
    # Group
    if (defined($changes{group})) {
      setGroup($ent, $changes{group});
      delete $changes{group};
    }
    # Icon
    if (defined($changes{icon}) && $changes{icon} =~ m/^\d+$/) {
      $ent->icon_id($changes{icon});
      delete $changes{icon};
    }
    # Standard strings
    my %kdbx_map = (
                title => 'Title',
                username => 'UserName',
                password => 'Password',
                url => 'URL',
                comment => 'Notes',
        );
    my %kdbx_map_rev = reverse %kdbx_map;
    foreach my $key (keys %changes) {
      if (! defined($kdbx_map{$key})) { next; } # Not a standard string
      my $chg_result = $ent->string($kdbx_map{$key}, $changes{$key});
      delete $changes{$key};
    }
    # Update the non-standard strings ("Additional attributes" in KeePassXC).
    if (defined($changes{strings})) {
      foreach my $key (keys %{$changes{strings}}) {
        if (defined($kdbx_map_rev{$key})) { next; } # Skip standard strings
        $ent->string($key, {	value => $changes{strings}->{$key},
				protect => $changes{protected}->{$key} // 0 } );
      }
      delete $changes{strings};
    }
    # Update the binaries (files)
    if (defined($changes{binary})) {
      foreach my $key (keys %{$changes{binary}}) {
        $ent->binary($key, {	value => $changes{binary}->{$key},
				protect => $changes{protected}->{$key} // 0 } );
      }
      delete $changes{binary};
    }
    delete $changes{protected} if exists($changes{protected});

    # Handle timestamp fields
    my %tm_map = (
        accessed         => 'last_access_time',
        created          => 'creation_time',
        modified         => 'last_modification_time',
        location_changed => 'location_changed',
        expires          => 'expiry_time',
	);
    foreach my $tm (keys %tm_map) {
      next if (! (exists($changes{$tm}) &&
		$changes{$tm} =~ m/^\d\d\d\d-\d\d-\d\d \d\d:\d\d:\d\d$/));
      my $kdbx_method = $tm_map{$tm};
      $ent->$kdbx_method($changes{$tm});
      delete($changes{$tm});
    }

    # Handle some other misc fields
    my %misc_map = (
        auto_type_enabled => 'auto_type_enabled',
        auto_type         => 'auto_type_associations',
        auto_type_munge   => 'auto_type_obfuscation',
        location_changed  => 'location_changed',
        expires_enabled   => 'expires',
        usage_count       => 'usage_count',
	foreground_color  => 'foreground_color',
	background_color  => 'background_color',
	);
    foreach my $misc (keys %misc_map) {
      next if (! exists($changes{$misc}));
      my $kdbx_method = $misc_map{$misc};
      $ent->$kdbx_method($changes{$misc});
      delete($changes{$misc});
    }

    # Things we skip/ignore
    # NOTE: File::KDBX makes its own history records.
    my @ignores = qw( history override_url protected );
    foreach my $ign (@ignores) {
      delete($changes{$ign}) if (exists($changes{$ign}));
    }

    # If we have an "otp" to update, do that here.
    if (defined($changes{otp})) {
      # If it is in URI format just store it, else convert it to
      # URI format and store it.
      my $new_otp = undef;
      if ($changes{otp} =~ m/^otpauth:/) {
        $new_otp = $changes{otp};
      } elsif (! is_loaded('URI')) {
        warn "Module URI (liburi-perl) is required.\n";
      } else {
        # https://github.com/google/google-authenticator/wiki/Key-Uri-Format
        my $ent_title = getLabel($ent);
        my $ent_uname = get_username($ent);
        my $uri = URI->new();
        $uri->scheme('otpauth');
        $uri->authority('totp');
        $uri->path($ent_title.':'.$ent_uname);
        $uri->query_form( secret => $changes{otp}, issuer => $ent_title, digits => 6 );
        $new_otp = $uri->as_string;
      }
      if (defined($new_otp)) {
        $ent->string('otp', value => $new_otp, protect => 1);
        delete($changes{otp});
      }
    }

    # We deleted update keys from %changes as we went and any that
    # are left in %changes we assume to be non-standard strings to
    # be updated.
    foreach my $key (keys %changes) {
      if (defined($kdbx_map_rev{$key})) { next; } # Skip standard strings
      if (ref($changes{$key}) ne '') { next; }    # Skip all non-scalars
      $ent->string($key, $changes{$key});
      delete($changes{$key});
    }

    if (scalar(keys %changes) > 0) {
      print "There appears to be a bug in update_entry()!\n";
      print "Leftover changes:\n".Dumper(\%changes)."\n"; # Intentional Dumper
    }

    # Commit the atomic transaction (makes a history record).
    # See File::KDBX::Object#begin_work documentation for details.
    $ent->commit;
  }
}

# A routine to copy entries to the /Backup or "/Recycle Bin" folders.
# Used by cli_edit, cli_rm, etc.
sub recycle_entry {
  my $state = shift @_;
  my $ent = shift @_;

  my $bugrp_id = get_recycle_group_uuid($state, 1);

  # If there is no group to recycle to, bail out now
  if (! defined($bugrp_id)) { return undef; }

  # We're not recycling already recycled entries!
  my $parent_group = get_parent_group_of_uuid($state->{kdb}, getID($ent));
  if ($bugrp_id eq getID($parent_group)) {
    return undef;
  }

  my $title_format="%s (%s)";
  my $add_result = undef;
  if (ref($state->{kdb}) eq 'File::KDBX') {
    my $rb_grp = get_group_by_uuid($state->{kdb},$bugrp_id);
    my $guard = $state->{kdb}->unlock_scoped; # Else can't clone protected strs
    my $new_ent = $ent->clone( new_uuid => 1, history => 1,
		reference_password => 0, reference_username => 0);
    my $lbl = sprintf($title_format, getLabel($ent), $ent->{modified});
    setLabel($new_ent, $lbl);
    $add_result = $rb_grp->add_entry($new_ent);
  } else {
    # File::KeePass method
    $state->{kdb}->unlock; # Required for the password field
    my $tmp_ent = clone($ent); # Clone the entry and back it up
    delete $tmp_ent->{id};
    # Append the modified time to the title for the backup dir.
    my $lbl = sprintf($title_format, getLabel($tmp_ent), $tmp_ent->{modified});
    setLabel($tmp_ent, $lbl);
    $tmp_ent->{modified} = $state->{kdb}->now;
    $tmp_ent->{group} = $bugrp_id;
    $add_result = $state->{kdb}->add_entry($tmp_ent);
    $state->{kdb}->lock;
  }

  if (! $add_result) {
    return "Failed to copy the entry to the backup folder.";
  } else {
    $state->{kdb_has_changed}=1;
  }
  refresh_state_all_paths();

  return undef; # Always undef if no errors, else $errmsg
}

# Returns /Backup or "/Recycle Bin" based on KeePass v1 or v2 file.
# Creates the group if it is missing and $create_if_missing in true.
sub get_recycle_group_uuid {
  my $state = shift @_;
  my $create_if_missing = shift @_ || 0;

  # Figure out what the path to the backup/recycle group is.
  my $bugrp = "/Backup"; # Default to v1 (is this correct?)
  if (ref($state->{kdb}) eq 'File::KeePass') {
    if ($state->{kdb_ver} == 2) {
      $bugrp = "/Recycle Bin";
    }
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    # NOTE: this call to ->recycle_bin() will "spring" one into
    # existance if ->recycle_bin_enabled is true (the default).
    # Because of that, I cannot reliably find the $bugrp by
    # using all_grp_paths_rev, thus the unusual code here.
    my $rb = $state->{kdb}->recycle_bin;
    my $root_name = getLabel($state->{kdb}->root, 1); # Cannot have utf8 here!
    if (defined($rb)) {
      my $rb_path = encode_if_utf8($rb->path, 1);     # Cannot have utf8 here!
      $rb_path =~ s%[.]%/%g;
      $bugrp = '/'.$root_name.'/'.$rb_path;
      # Because File::KDBX may have "autovivified" this group when we
      # called ->recycle_bin(), we may need to refresh_state_all_paths()
      if (! defined($state->{all_grp_paths_rev}->{$rb->uuid})) {
        refresh_state_all_paths();
      }
      if (! defined($state->{all_grp_paths_rev}->{$rb->uuid})) {
        warn "Apparent bug in get_recycle_group_uuid(). Please report it.\n";
        return undef;
      }
    } else {
      $bugrp = '/'.$root_name.'/Recycle Bin';
    }
  }

  my $grp_path = normalize_path_string($bugrp); # For lookups
  if ($create_if_missing) {
    if (! defined($state->{all_grp_paths_fwd}->{$grp_path})) {
      my $title = basename($bugrp);
      my $new_group = addGroup($state->{kdb},undef,{title => $title});
      refresh_state_all_paths();
      $state->{kdb_has_changed}=1;
    }
  }
  if (! defined($state->{all_grp_paths_fwd}->{$grp_path})) {
    return undef;
  }
  return $state->{all_grp_paths_fwd}->{$grp_path};
}

# Helper function for cli_edit() and cli_clone()
sub _entry_edit_gui($$$) {
  my $ent=shift @_;
  my $rChanges = shift @_;
  my $kdb_ver = shift @_;

  # Make a entry hash for simple changes
  $state->{kdb}->unlock;
  my $enth = entry_as_hash($ent);
  $state->{kdb}->lock;

  # Loop through the fields taking edits the user wants to make
  my @fields = get_entry_fields($kdb_ver);
  FIELD: foreach my $input (@fields) {
    my $current_val = $enth->{$input->{key}};
    my $val = undef;
    if (defined($input->{user_prep_func})) {
      $current_val = $input->{user_prep_func}($current_val);
    }
    if (defined($input->{edit_entry_strings_func})) {
      my $tmp_ent = $ent;
      # NOTE: we pass an $ent clone here, not the $enth
      if (ref($ent) =~ m/File::KDBX::/) {
        my $guard = $state->{kdb}->unlock_scoped; # Else can't clone protected strs
        $tmp_ent = $ent->clone( new_uuid => 1, history => 0,
		reference_password => 0, reference_username => 0);
      }
      my $chg_ent = $input->{edit_entry_strings_func}($tmp_ent, $input, $current_val);
      # We handle changes for this section (strings) completely differently
      # than all other fields because File::KeePass stores its hash of
      # protected strings separately ($ent->{strings}->{k} and $ent->{protected}),
      # while File::KDBX stored them together ($ent->{strings}->{k}->{value} and
      # $ent->{strings}->{k}->{protect}). In this instance, if no changes are
      # made we get undef, else we get back a temp ent that we pull from.
      if (defined($chg_ent)) {
        # "$input->{key}" could be written as "strings" ...
        $rChanges->{$input->{key}} = $chg_ent->{$input->{key}};
        if (ref($ent) !~ m/File::KDBX::/ && exists($chg_ent->{protected})) {
          $rChanges->{protected} = $chg_ent->{protected}; # File::KeePass
        }
      }
      next FIELD; # Because we handle changes differently here...
    } elsif ($input->{multiline}) {
      $val = new_edit_multiline_input($input, $current_val);
    } else {
      $val = new_edit_single_line_input($input, $current_val);
    }
    # If the user hit ^C (SIGINT) then we need to stop
    if (recent_sigint()) { return -1; }
    # Call the validate_func if it's defined
    if (defined($input->{validate_func}) && defined($val)) {
      # Note that $val can be modified by the validate_func
      if ($input->{validate_func}(\$val) != 0) {
        print "Invalid $input->{txt} input.\n";
        return -1;
      }
    }
    # Check a new title for same-name conflicts in its group
    if ($input->{key} eq 'title' && defined($val)) {
      if ($val =~ m/\//) {
        print "kpcli cannot support titles with slashes (/) in them.\n";
        return -1;
      }

      my $parent = get_parent_group_of_uuid($state->{kdb},getID($ent));
      my $path = get_path($parent);
      my $val_not_utf8 = encode_if_utf8($val);
      my $new_entry = normalize_path_string("$path/$val_not_utf8");
      if (defined($state->{all_ent_paths_fwd}->{$new_entry})) {
        print "An entry titled \"$val\" is already in $path.\n";
        return -1;
      }
    }
    # If the field was not undefined, we'll change it to the new $val
    if (defined($val)) { $rChanges->{$input->{key}} = $val; }
  }
  return 0;
}


# A code-consolidation function...
sub get_prepped_readline_term() {
  our $state;

  # Note: A 2nd Term::ReadLine::Gnu->new() just returns the same
  # object as the one that Term::ShellUI is already using. With
  # Term::Readline::Perl, an attempt to call new a 2nd time results
  # in having a Term::Readline::Stub returned and a warning printed to
  # STDERR, which we also don't want, and so I coded this the way that
  # I did to make clear what is being done, and this comment for why.
  my $term = $state->{term}->{term}; # Term::ShellUI's readline
  $state->{active_readline} = $term;

  # Use Term::ReadLine::Gnu more advanced functionality...
  if ($term->ReadLine() eq 'Term::ReadLine::Gnu') {
    # Called roughly 10-times per second while Gnu readline waits for input
    $term->Attribs->{event_hook} = sub {
          if (recent_sigint()) {
             $term->Attribs->{event_hook} = undef;
             $term->set_prompt('');
             $term->Attribs->{line_buffer}='';
             $term->Attribs->{done} = 1;
	     $state->{active_readline} = undef;
          }
        };
  }

  return $term;
}

# A helper function to interactively edit an entry's strings
sub edit_entry_strings {
  my $ent = shift @_;
  my $input = shift @_;
  my $initial_value = shift @_;
  our $state;

  # We make a clone of the $ent that we were passed to operate on and we
  # return it (with our modifications within it) if anything is changed.
  my $tmp_ent = undef;
  if (ref($ent) =~ m/^File::KDBX::/) {
    my $guard = $state->{kdb}->unlock_scoped; # Else can't clone protected strs
    $tmp_ent = $ent->clone( new_uuid => 1, history => 0,
		reference_password => 0, reference_username => 0);
  } else {
    $tmp_ent = clone($ent); # Clone the entity
  }

  my $changes_made = 0;
  EDIT_INTERFACE: while (1) {
    # Make an $enth from $tmp_ent that gets used below, and it must be remade
    # on each loop cycle to capture any changes that are made.
    $state->{kdb}->unlock;
    my $enth = entry_as_hash($tmp_ent);
    $state->{kdb}->lock;

    my @strings_keys = ();
    if (defined($enth->{strings}) && ref($enth->{strings}) eq 'HASH') {
      @strings_keys = sort keys %{$enth->{strings}};
    }
    my $strings_count = scalar(@strings_keys);
    my $t='';
    my $prompt = "Strings";
    if ($strings_count > 0) {
      $t .= show_helper_files_strings($enth,{f=>1,v=>1},'strings');
      $prompt = "Choose";
    }
    $t .= "$prompt: (a)dd/(e)dit/(d)elete/(p)rotect/(c)ancel/(F)inish? ";
    print "$t";
    COMMAND: while (my $key=get_single_key()) {
      if (lc($key) eq 'c' || ord($key) == 3) { # Cancel or ^C
        print "\n";
        return undef; # We are to return undef on no change
      } elsif ($key =~ m/^[fF\r\n]$/) { # Finished (save)
        print "\n";
        if ($changes_made) {
          return $tmp_ent; # Changes made and $tmp_ent holds them
        } else {
          return undef; # No changes made
        }
      } elsif (lc($key) eq 'd') {
        if (defined($tmp_ent->{strings}) &&
					ref($tmp_ent->{strings}) eq 'HASH') {
          if ($strings_count == 1) {
            %{$tmp_ent->{strings}} = ();
            $changes_made = 1;
          } else {
            print "\r". " "x60 ."\rWhich entry number do you want to delete? ";
            my $choice = get_single_line();
            if ($choice !~ m/^\d+$/ || $choice<1 || $choice > $strings_count) {
              print "\nInvalid number.";
            } else {
              delete($tmp_ent->{strings}->{$strings_keys[$choice-1]});
              $changes_made = 1;
            }
          }
          print "\n";
          next EDIT_INTERFACE;
        }
      } elsif (lc($key) =~ m/^p$/) {
        if ($strings_count < 1) {
          print "\nNo strings to toggle protection on.\n";
          next EDIT_INTERFACE;
        } else {
          my $choice = 0;
          if ($strings_count > 1) {
            print "\r". " "x60 ."\rWhich entry number do you want to toggle? ";
            $choice = get_single_line();
          } elsif ($strings_count == 1) {
            $choice = 1;
          }
          if ($choice !~ m/^\d+$/ || $choice<1 || $choice > $strings_count) {
            print "\nInvalid number.\n";
            next EDIT_INTERFACE;
          }

          # Toggle protect on the $choice field
          my $fld = $strings_keys[$choice-1];
          # Get current protected state
          my $protected = 0; # Default to not protected
          my $val = $tmp_ent->{strings}->{$fld}; # File::KeePass has scalar here
          # Set $protected for this ent if we can
          if (ref($val) eq 'HASH') {       # File::KDBX has a hash here
            if (exists($val->{protect})) {
              $protected = $val->{protect}; # Should be 0|1
            }
          } elsif (defined($tmp_ent->{protected}) &&      # File::KeePass v2 DBs
                ref($tmp_ent->{protected}) eq 'HASH') {
            $protected = $tmp_ent->{protected}->{$fld} // 0;
          }

          # Toggle the protected state and set that for this $fld
          my $new_prot = ($protected + 1) % 2; # Toggle for the new state
          if (ref($val) eq 'HASH') {       # File::KDBX has a hash here
            $val->{protect} = $new_prot;
          } else {   # File::KeePass v2 DBs
            $tmp_ent->{protected}->{$fld} = $new_prot;
            #print "LHHDp: ".Dumper($tmp_ent->{protected},$ent->{protected})."\n";
          }
          #print "\nToggled protection on string $choice from $protected to $new_prot\n";

          $changes_made = 1;
          print "\n";
          next EDIT_INTERFACE;
        }
      } elsif (lc($key) =~ m/^[ae]$/) {
        my $iv='';
        my $fld_being_edited = undef;
        if (lc($key) eq 'e' && $strings_count > 0) {
          my $choice = 0;
          if ($strings_count > 1) {
            print "\r". " "x60 ."\rWhich entry number do you want to edit? ";
            $choice = get_single_line();
          } elsif ($strings_count == 1) {
            $choice = 1;
          }
          if ($choice !~ m/^\d+$/ || $choice<1 || $choice > $strings_count) {
            print "\nInvalid number.";
            print "\n";
            next EDIT_INTERFACE;
          }
          $fld_being_edited = $strings_keys[$choice-1];
          my $val_being_edited = $tmp_ent->{strings}->{$fld_being_edited};
          $iv = "$fld_being_edited = $val_being_edited";
        }
        my $prompt = "Input a key=value pair: ";
        print "\r". " "x60 ."\r";
        my $term = get_prepped_readline_term();
        my $keyval = $term->readline($prompt, $iv);
        $keyval = decode_if_not_utf8($keyval) if ($ALL_USER_INPUT_TO_UTF8);
        if ($keyval =~ m/^\s*([^=]+?)\s*=\s*(.+?)\s*$/) {
          my ($fld, $val) = ($1, $2);
          if (!(defined($tmp_ent->{strings})) &&
					ref($tmp_ent->{strings}) eq 'HASH') {
            $tmp_ent->{strings} = {};
            $changes_made = 1;
          }
          if (defined($tmp_ent->{strings}->{$fld}) &&
			(lc($key) eq 'a' || $fld ne $fld_being_edited)) {
            print "\nString field \"$fld\" already exists in the entry.";
          } else {
            $tmp_ent->{strings}->{$fld}=$val;
            $changes_made = 1;
            if (defined($fld_being_edited) && $fld ne $fld_being_edited) {
              delete($tmp_ent->{strings}->{$fld_being_edited});
            }
          }
        } else {
          print "\nInvalid entry.";
        }
        print "\n";
        next EDIT_INTERFACE;
      } else {
        # Do nothing on invalid input
        next COMMAND;
      }
    }
  }

  return $initial_value;
}
# Single line input helper function for cli_new and cli_edit.
sub new_edit_single_line_input($$) {
  my $input = shift @_;
  my $initial_value = shift @_;
  our $state;

  # The password is a special case in that we don't show it, nor allow
  # the user to edit it, only "replace" it. As such, if the password
  # comes in here, we need to emtpy it.
  if ($input->{key} eq 'password') {
    $initial_value = '';
  }

  my $iv = ''; if (! $input->{hide_entry}) { $iv = $initial_value; }
  my $term = get_prepped_readline_term();
  my $val = '';

  PASSWD_COLLECTION: {
    if ($input->{genpasswd}) {
      print " "x25 .'("g" or "w" to auto-generate, "i" for interactive)'. "\r";
    }
    my $prompt=$input->{txt} . ': ';
    if ($input->{hide_entry}) {
      $val = GetPassword($prompt, '');
    } else {
      $val = $term->readline($prompt, $iv);
    }
    chomp $val;
    if ($input->{genpasswd} && $val =~ m/^([wgi])(\d*)$/) {
      my $cmd = $1;
      my $len = $2;
      if ($cmd eq 'g' || $cmd eq 'i') {
        if (!$len) {
          $len = $DEFAULT_PASSWD_LEN;
        } elsif ($len !~ m/^\d+$/ ||
		$len < $DEFAULT_PASSWD_MIN || $len > $DEFAULT_PASSWD_MAX) {
          $len = $DEFAULT_PASSWD_LEN;
          print color('yellow')
              . "Password length out of bounds, reset to $len chars.\n"
              . color('clear');
        }
        if ($cmd eq 'g') {
          $val = generatePasswordGobbledygook($len);
        } elsif ($cmd eq 'i') {
          $val = generatePasswordInteractive($len);
          # Interactive canceled by user
          if (! defined($val)) {
            print "\n";
            redo PASSWD_COLLECTION;
          }
        }
      } elsif ($cmd eq 'w') {
        $val = generatePassword();
      } else {
        die "BUG: it should be impossible to get to this code!\n";
      }
    } elsif (length($val) && $input->{double_entry_verify}) {
      my $prompt = "Retype to verify: ";
      my $checkval = '';
      if ($input->{hide_entry}) {
        $checkval = GetPassword($prompt, '');
      } else {
        $checkval = $term->readline($prompt);
      }
      # If the user hit ^C (SIGINT) then we need to stop
      if (recent_sigint()) { return undef; }
      chomp $checkval;
      if ($checkval ne $val) {
        print "Entries mismatched. Please try again.\n";
        redo PASSWD_COLLECTION;
      }
    }
  }
  # We are done with readline calls so let's cleanup.
  if ($term->ReadLine() eq 'Term::ReadLine::Gnu') {
    $term->Attribs->{startup_hook} = undef;
    $term->Attribs->{event_hook} = undef;
  }

  $val = decode_if_not_utf8($val) if ($ALL_USER_INPUT_TO_UTF8);

  # This is a strange exception for File::KeePass, but it is required for the
  # password field to be compatible with other programs. What we do here encode
  # back to a bytestring after we decoded to UTF-8 just above. If we don't do
  # that, then we end up with the first type of string instead of the second and
  # that is a problem:
  #   "password" => "entry-G\351n\351ral-1p",
  #   "password" => "entry-G\303\251n\303\251ral-1p",
  # I think this is related to the use of GetPassword() above, which uses raw
  # input via Term::ReadKey instead of readline, which is how all of the other
  # fields above are collected.
  if ($input->{key} eq 'password' && ref($state->{kdb}) eq 'File::KeePass') {
    #print "LHHD: val=$val is_utf8=".int(utf8::is_utf8($val))."\n";
    my $new_val = encode_if_utf8($val);
    #print "LHHD: new_val=$new_val is_utf8=".int(utf8::is_utf8($new_val))."\n";
    $val = $new_val;
  }

  # This function is supposed to return undef if nothing changed.
  if (eq_w_utf8_check($val,$initial_value)) { $val = undef; }

  return $val;
}
# Multi-line input helper function for cli_new and cli_edit.
sub new_edit_multiline_input($$) {
  my $input = shift @_;
  my $initial_value = shift @_;
  our $state;

  # Protect programmers from accidentally misusing this function
  if ($input->{genpasswd}) { die "genpasswd unsupported by this function"; }
  if ($input->{password}) { die "password unsupported by this function"; }

  if ($input->{hide_entry}) {
    print $input->{txt} . ": ";
  } else {
    my $mlval = $initial_value;
    if ($mlval =~ m/\r|\n/) { $mlval = "\n$mlval\n"; }
    print $input->{txt} . " (\"".$mlval."\"): ";
  }

  my $yellow=color('yellow');
  my $clear=color('clear');
  print "\n$yellow(end multi-line input with a single \".\" on a line)$clear\n";

  my $term = get_prepped_readline_term();

  my $val = ''; my $unfinished = 1;
  while ($unfinished) {
    # Term::ReadLine::Perl seems to have a bug that requires a prompt
    # (it borks on ''), but after adding the pipe I liked it so left
    # it place for all readlines.
    my $line = $term->readline('| ');
    if (! defined($line)) {   # Handles user hitting Ctrl-D
      print "\r";
      next;
    }
    if ($line =~ m/^\.[\r\n]*$/) { # a lone "." ends our input
      $unfinished = 0;
    } else {
      $line .= "\n" if ($line !~ m/\n$/); # ReadLine() vs. $term->readline().
      $val .= $line;
      if ($val =~ m/^[\r\n]*$/) { $val = ''; $unfinished = 0; }
    }
    # If the user hit ^C (SIGINT) then we need to stop
    if (recent_sigint()) { return undef; }
  }
  chomp($val); # Remove extra line at the end

  $val = decode_if_not_utf8($val) if ($ALL_USER_INPUT_TO_UTF8);

  # This function is supposed to return undef if nothing changed.
  # In this multi-line edit function, no change is ''.
  if (eq_w_utf8_check($val,'')) { $val = undef; }

  return $val;
}

# Formats an entry for display for cli_show()
sub show_format($$) {
  my $title=shift @_;
  my $value=shift @_;
  my $val=$value // '';
  if ($val =~ m/\n/) {
    my @val_lines=split(/\n/, $val);
    $val=join("\n" . " "x(5+2), @val_lines);
  }
  return sprintf("%5s: %s", $title,$val);
}

# Formats a statistic display for cli_stats()
sub stats_print($) {
  my $stats_r = shift @_;

  my $max_key_len = 0;
  my $max_val_len = 0;
  foreach my $k (keys(%{$stats_r})) {
    if (length($k) > $max_key_len) { $max_key_len = length($k); }
  }
  foreach my $k (values(%{$stats_r})) {
    if (length($k) > $max_val_len) { $max_val_len = length($k); }
  }
  my $sprintf_format = "  - %$max_key_len" . "s: %$max_val_len" . "d\n";
  my $t='';
  foreach my $stat_key (sort {toint($a) <=> toint($b)} keys %{$stats_r}) {
    $t .= sprintf($sprintf_format, $stat_key, $stats_r->{$stat_key});
  }
  return $t;
}
# Helper function for stats_print()
sub toint($) {
  my $range = shift @_;
  if ($range =~ m/^[0-9]+$/) { return $range; }		# 0
  if ($range =~ m/^([0-9]+)-[0-9]+$/) { return $1; }	# 1-7
  if ($range =~ m/^([0-9]+)[+]$/) { return $1; }	# 20+
  # We should never get here, but if we do, this is the fallback
  my $retval = $range;
  $retval =~ s/[^0-9]//g;
  return $retval;
}

# Helper functions to normalize and humanize entry tags
sub normalize_entry_tags {
  my $rTagline = shift @_;
  my @tags = split(/\s*[;,]\s*/, $$rTagline);
  $$rTagline = join(';', @tags);
  return 0;
}
sub humanize_entry_tags {
  my $tagline = shift @_;
  my @tags = split(/\s*[;,]\s*/, $tagline);
  return join(', ', @tags);
}

# Function to return a data structure to support adding/editing entries
sub get_entry_fields {
  my $kdb_ver = shift @_ || 1; # *.kdb or *.kdbx (v1 or v2)
  my @fields = (
	{ key=>'title', txt=>'Title' },
	{ key=>'username', txt=>'Username' },
	{ key=>'password', txt=>'Password',
		hide_entry => 1, double_entry_verify => 1, genpasswd => 1 },
	{ key=>'url', txt=>'URL' },
  );
  # We only want "tags" if we are dealing with a v2 file (*.kdbx)
  if ($kdb_ver == 2) {
    push @fields, (
	{ key=>'tags', txt=>'Tags', 'multiline' => 0,
		user_prep_func => \&humanize_entry_tags,
		validate_func => \&normalize_entry_tags,
	 },
	{ key=>'strings', txt=>'Strgs',
		edit_entry_strings_func => \&edit_entry_strings,
	 },
	);
  }
  push @fields, (
	{ key=>'comment', txt=>'Notes/Comments', 'multiline' => 1 },
	);
  return @fields;
}

# Code consolidation function.
# Returns true if $state->{signals}->{INT} indicates a SIGINT more
# recently than the $timeframe given, which defaults to 0.25 secs.
sub recent_sigint() {
  my $timeframe = shift @_ || 0.25;
  if ($timeframe !~ m/^([0-9]*\.[0-9]+|[0-9]+)$/) { $timeframe = 0.25; }
  our $state;
  if (defined($state->{signals}->{INT}) &&
		tv_interval($state->{signals}->{INT}) < $timeframe) {
    return 1;
  }
  return 0;
}

sub cli_icons($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  print "Change icons on Groups or Entries (g/e/Cancel)? ";
  my $groups_or_entries=lc(get_single_key());
  print "\n";
  if (recent_sigint() || $groups_or_entries !~ m/^[ge]$/) { return; }

  print "Change icons Here, Below here, or Globally (h/b/g/Cancel)? ";
  my $glob_or_rel=lc(get_single_key());
  print "\n";
  if (recent_sigint() || $glob_or_rel !~ m/^[hgb]$/) { return; }

  print "What would you line the new icon to be (0-64/Cancel)? ";
  my $term = get_prepped_readline_term();
  my $val = $term->readline('');
  # If the user hit ^C (SIGINT) then we need to stop
  if (recent_sigint()) { return undef; }
  chomp($val);
  if ($val !~ m/^[0-9]+$/ || $val < 0 || $val > 64) {
    print "Invalid icon number.\n";
    return;
  }

  # This code fills @{$groups} or @{$entries} with the items that the
  # user wants to change the icons on.
  my ($groups,$entries) = ([],[]);
  if ($glob_or_rel eq 'h') { # "Here" is easy -- we have a function for that.
    my $norm_path = normalize_path_string(get_pwd());
    if (length($norm_path)) { # Any path other than /
      my $id=$state->{all_grp_paths_fwd}->{$norm_path};
      ($groups,$entries) = get_kids_by_group_uuid($state->{kdb}, $id);
    } else {
      @{$groups} = get_root_groups($state->{kdb});
    }
    if ($groups_or_entries eq 'e') {
      $groups = [];
    } else {
      $entries = [];
    }
  } else {
    if ($glob_or_rel eq 'g') { # Globally is easy, it's all groups
      my $k = $state->{kdb};
      @{$groups} = get_all_groups($k);
    } elsif ($glob_or_rel eq 'b') {
      my $id = $state->{path}->{id};
      @{$groups} = all_child_groups_flattened($id); # *only child groups*
    } else {
      warn "WHAT? Should never get to this piece of code!\n";
    }
    # If the user wanted to operate on entries, collect all the entries
    # in the @{$groups} and then empty @{$groups}.
    if ($groups_or_entries eq 'e') {
      foreach my $group (@{$groups}) {
        if (defined($group->{entries})) {
          push @{$entries}, @{$group->{entries}};
        }
      }
      $groups = [];
    }
  }

  # Change the items, recording the number of changes.
  my $items_changed=0;
  foreach my $item (@{$groups}, @{$entries}) {
    if (ref($state->{kdb}) eq 'File::KeePass') {
      $item->{icon} = $val;
    } elsif (ref($state->{kdb}) eq 'File::KDBX') {
      $item->icon_id($val);
    }
    $items_changed++;
  }

  # Tell the user what we did.
  print "The icon value was set to $val on $items_changed records.\n";

  # If we changed anything, ask the user if they want to save
  if ($items_changed > 0) {
    $state->{kdb_has_changed}=1;
    RequestSaveOnDBChange();
  }
  return 0;
}

sub cli_new($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $new_path=get_pwd();
  my $new_title='';
  # If the user gave us a path (that may include the new title) in args[0],
  # then we have to first rationalize that path.
  if (defined($params->{args}->[0])) {
    $new_path = $params->{args}->[0];
    # Insure that $new_path is absolute
    if ($new_path !~ m/^\/+$/) {
      $new_path = get_pwd() . '/' . $new_path;
    }
    my $norm_path = normalize_path_string($new_path);
    my ($grp_path,$name)=normalize_and_split_raw_path($new_path);
    if (defined($state->{all_grp_paths_fwd}->{$norm_path})) {
      $new_path = '/' . humanize_path($norm_path);
      $new_title = '';
    } elsif (defined($state->{all_grp_paths_fwd}->{$grp_path})) {
      $new_path = '/' . humanize_path($grp_path);
      $new_title = $name;
    } else {
      if ($norm_path eq '') {
        print "Entries cannot be made in the root path.\n";
      } else {
        print "Bad path for new entry\n";
      }
      return;
    }
  }
  $new_title = decode_if_not_utf8($new_title) if ($ALL_USER_INPUT_TO_UTF8);
  $new_path = encode_if_utf8($new_path, 1);

  # $id needs to be set to the ID of the group we want to add to
  my $id = undef;
  my $norm_path=normalize_path_string($new_path);
  if (defined($state->{all_grp_paths_fwd}->{$norm_path})) {
    $id=$state->{all_grp_paths_fwd}->{$norm_path};
  }

  # Make sure that we have a valid path for creating a new entry
  if ($new_path =~ m/^\/+$/ || (! defined($id))) {
    print "Entries cannot be made in this path ($new_path).\n";
    return -1;
  }

  print "Adding new entry to \"$new_path\"\n";

  my $k=$state->{kdb};

  my $new_entry = {
    'group' => $id,
  };

  my @fields = get_entry_fields($state->{kdb_ver});
  NEW_DATA_COLLECTION: foreach my $input (@fields) {
    my $val = '';
    if (defined($input->{edit_entry_strings_func})) {
      $val = $input->{edit_entry_strings_func}($new_entry, $input, {});
      # An empty hash-ref is "empty/blank" for strings, but here, for a
      # new entry, the edit_entry_strings_func returns undef in that case (no change).
      if ($input->{key} eq 'strings') {
        $new_entry->{strings} = {} if (!defined($val)); # Empty hashref
        if (defined($val) && ref($val) eq 'HASH') {
          foreach my $k (qw(strings protected)) {
            $new_entry->{$k} = $val->{$k} if(exists($val->{$k}));
          }
        }
        #print "LHHDxx: val=".Dumper($val)."\n";
        # We handle setting $new_entry values here completely differently
        # than other parts of this loop (for protected) and thus next now.
        next NEW_DATA_COLLECTION;
      }
    } elsif ($input->{multiline}) {
      # If the user does not change the default input, undef is returned,
      # thus the need for the "|| ''" at the end of this.
      $val = new_edit_multiline_input($input, '') || '';
    } else {
      if ($new_title ne '' && $input->{key} eq 'title') {
        print $input->{txt} . ": $new_title\n";
        $val = $new_title;
      } else {
        # If the user does not change the default input, undef is returned,
        # thus the need for the "|| ''" at the end of this.
        $val = new_edit_single_line_input($input, '') || '';
      }
    }
    # If the user hit ^C, abort the new entry
    if (recent_sigint()) { return undef; }
    # If the user gave us an empty title, abort the new entry
    if ($input->{key} eq 'title' && length($val) == 0) { return undef; }
    # Call the validate_func if it's defined
    if (defined($input->{validate_func}) && length($val)) {
      # Note that $val can be modified by the validate_func
      if ($input->{validate_func}(\$val) != 0) {
        print "Invalid $input->{txt} input.\n";
        return -1;
      }
    }
    # Check the new title for same-name conflicts in its group
    if ($input->{key} eq 'title') {
      if ($val =~ m/\//) {
        print "kpcli cannot support titles with slashes (/) in them.\n";
        return undef;
      }
      # $val is utf8 so we must encode it prior to normalize_path_string()
      my $new_ent_full_path = $new_path . '/' . encode_if_utf8($val, 1);
      my $new_entry = normalize_path_string($new_ent_full_path);
      if (defined($state->{all_ent_paths_fwd}->{$new_entry})) {
        print "An entry titled \"$val\" is already in $new_path.\n";
        return undef;
      }
    }

    $new_entry->{$input->{key}} = $val;
  }

  my $new_entry_uuid = addEntry($k, $new_entry);
  if (defined($new_entry_uuid)) {
    refresh_state_all_paths();
    $state->{kdb_has_changed}=1;
    RequestSaveOnDBChange();
  } else {
    print "Failed to add new entry.\n";
  }
  return 0;
}

sub addEntry {
  my $k = shift @_; # $self->{kdb}
  my $new_entry = shift @_;
  our $state;

  $new_entry->{icon} = $DEFAULT_ENTRY_ICON;

  my $new_entry_uuid = undef;
  if (ref($k) eq 'File::KeePass') {
    $k->unlock;
    my $new_entry_ref = $k->add_entry($new_entry);
    $k->lock;
    if (defined($new_entry_ref)) { $new_entry_uuid = getID($new_entry_ref); }
  } elsif (ref($k) eq 'File::KDBX') {
    my $parent_group = get_group_by_uuid($k, $new_entry->{group});
    my $ent = $parent_group->add_entry(); # An empty entry in $parent_group
    if (defined($ent)) {
      update_entry($k, $ent, $new_entry); # $new_entry == \%changes
      $new_entry_uuid = $ent->uuid;
    }
  }

  if (defined($new_entry_uuid)) {
    return $new_entry_uuid;
  } else {
    return undef;
  }
}

sub cli_import {
  my $file=shift @_;
  my $new_group_path=shift @_;
  my $key_file=shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly()) { return; }

  # If the user gave us a bogus file there's nothing to do
  if (! -f ($file)) {
    print "File does not exist: $file\n";
    return -1;
  }
  my $import_file_type = magic_file_type($file);
  if (scalar(grep(/^$import_file_type$/, qw(keepass pws3))) != 1) {
    print "Does not appear to be a KeePass or Password Safe v3 file: $file\n";
    return -1;
  }
  # If the $new_group_path is a relative path, make it absolute
  if ($new_group_path !~ m/^\//) {
    $new_group_path = get_pwd() . "/$new_group_path";
  }
  # We won't import into an existing group
  my $full_path=normalize_path_string($new_group_path);
  if (defined($state->{all_grp_paths_fwd}->{$full_path})) {
    print "You must specify a _new_ group to import into.\n";
    return -1;
  }
  # Make sure the new group's parent exists
  my ($grp_path,$grp_name)=normalize_and_split_raw_path($new_group_path);
  if ($grp_path ne '' && ! defined($state->{all_grp_paths_fwd}->{$grp_path})) {
    print "Path does not exist: /" . humanize_path($grp_path) . "\n";
    return -1;
  }
  # Set the $parent_group value appropriately
  my $parent_group = undef; # Root by default
  if (length($grp_path)) {
    $parent_group = $state->{all_grp_paths_fwd}->{$grp_path};
  }
  # Ask the user for the master password and then open the kdb
  my $master_pass=GetMasterPasswd();
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  if ($import_file_type eq 'keepass') {
    return cli_import_keepass($file,
			$master_pass,$key_file,$grp_name,$parent_group);
  } elsif ($import_file_type eq 'pws3') {
    return cli_import_pwsafe3($file,
			$master_pass,$key_file,$grp_name,$parent_group);
  } else {
    print "Unsupported file type for import.\n";
    return -1;
  }
}

sub cli_import_pwsafe3 {
  my $file = shift @_;
  my $master_pass = shift @_;
  my $key_file = shift @_;
  my $grp_name = shift @_;
  my $parent_group = shift @_;
  our $state;

  # This requires Crypt::PWSafe3 so try to load it if we don't have it
  if  (! is_loaded('Crypt::PWSafe3')) {
    runtime_load_module(\%OPTIONAL_PM,'Crypt::PWSafe3',[qw(capture)]);
  }
  if  (! is_loaded('Crypt::PWSafe3')) {
    print "Perl module Crypt::PWSafe3 is required for this functionality.\n";
    return -1;
  }

  # The eval is needed to catch the output of Carp::croak from Crypt::PWSafe3
  my $pws3;
  eval { $pws3 = new Crypt::PWSafe3(file => $file,
			password => $master_pass, program  => $APP_NAME); };
  if ($@ || ref($pws3) ne 'Crypt::PWSafe3') {
    print "Failed to load $file.";
    if ($@ =~ m/^Wrong password/i) {
      print " Wrong password.\n";
    } else {
      print "Error: $@\n";
    }
    return -1;
  }
  my @records = $pws3->getrecords();
  if (scalar(@records) < 1) { print "No records to import.\n"; return -1; }
  # Find any groups in the pws3 file that we need to create, and make them
  my @groups = ();
  foreach my $record (@records) { push @groups, $record->group(); }
  @groups = grep(!/^$/, @groups); # eliminate the top-level (empty) group

  # Add the new group, to its parent or to root if $parent_group==undef
  my $k=$state->{kdb};
  my $new_group = addGroup($k,$parent_group,{title => $grp_name});
  # %new_groups will hold new groups that we add during this import,
  # indexed by the PWSafe3 group name, like "foo.bar.baz"
  my %new_groups = ();
  $new_groups{""} = $new_group; # Top level group for this import

  @groups = sort(uniq(@groups)); # sort is critical to the algorithm just below
  #print "LHHD: " . &Dumper(\@groups) . "\n";
  foreach my $group (@groups) {
    my @group_tree = split(/[.]/, $group);
    #print "LHHD: " . &Dumper(\@group_tree) . "\n";
    my $child_group = pop @group_tree;
    my $new_group_pws3_path = join(".", @group_tree);
    my $pws3_parent_group = $new_group; # default to new parent group
    if (defined($new_groups{$new_group_pws3_path})) {
      $pws3_parent_group = $new_groups{$new_group_pws3_path};
    }
    #print "LHHD: need2make *$child_group* under *$new_group_pws3_path*\n";
    #print "LHHD: creating $child_group under $pws3_parent_group\n";
    $new_groups{$group} = addGroup($k,$pws3_parent_group,{title => $child_group});
  }

  # The new group(s) are made, now insert the records...
  $k->unlock();
  foreach my $record (@records) {
    my $pws3_group = $record->group();
    my $new_entry = {
      'group'    => $new_groups{$pws3_group},
      'title'    => $record->title(),
      'username' => $record->user(),
      'password' => $record->passwd(),
      'comment'  => $record->notes(),
      'url'      => $record->url(),
      'created'  => strftime("%Y-%m-%d %H:%M:%S",localtime($record->ctime())),
      'modified' => strftime("%Y-%m-%d %H:%M:%S",localtime($record->mtime())),
      'accessed' => strftime("%Y-%m-%d %H:%M:%S",localtime($record->atime())),
      'expires'  => strftime("%Y-%m-%d %H:%M:%S",localtime($record->pwexp())),
    };
    $k->add_entry($new_entry);
    #print "LHHD: " . &Dumper($record) . "\n";
  }
  $k->lock();

  # Refresh all paths and mark state as changed
  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();
}

sub cli_import_keepass {
  my $file = shift @_;
  my $master_pass = shift @_;
  my $key_file = shift @_;
  my $grp_name = shift @_;
  my $parent_group = shift @_;
  our $state;

  if (deny_if_readonly()) { return; }

  my $finf = kp_file_info($file); # importing file info

  my $k=$state->{kdb}; # The File::KeePass or File::KDBX we're importing into
  my $iKDB = undef; # Will hold the importing File::KeePass or File::KDBX
  my @root_groups = ();

  # Import KDBX4 files with either import_KDBX4_KeePassXC() or File::KDBX
  if ($finf->{version} == 2 and $finf->{kdbx_ver} >= 4.0) {
    # If we don't have File::KDBX, just shunt off to import_KDBX4_KeePassXC(),
    # which does its own error handling if KeePassXC is not available.
    if (! is_loaded('File::KDBX')) {
      return import_KDBX4_KeePassXC($file,$master_pass,$key_file,$grp_name,$parent_group);
    }
    # Load importing file with File::KDBX
    $iKDB = File::KDBX->new;
    my $comp_master_key = composite_master_pass('File::KDBX', $master_pass, $key_file);
    if (! eval { $iKDB->load_file($file, $comp_master_key); }) {
      my $error = File::KDBX::Error->error($@);
      my $details = $error->details;
      #print Dumper($details)."\n";
      if (defined($error->{error})) {
        return "Errors from File::KDBX:\n$error->{error}\n";
      }
    }
    $root_groups[0] = $iKDB->root; # Only one root in KDBXv4
  } else {
    # Import v1 and v2 through KDBX version 3.1
    # Load importing file with File::KeePass
    $iKDB = File::KeePass->new;
    my $comp_master_key = composite_master_pass('File::KeePass', $master_pass, $key_file);
    if (! eval { $iKDB->load_db($file, $comp_master_key); } ) {
      print "Couldn't load the file $file: $@\n";
      return -1;
    }
    @root_groups = get_root_groups($iKDB);
  }

  # Add the new group, to its parent or to root if $parent_group==undef
  my $new_group = addGroup($k,$parent_group,{title => $grp_name});

  {
    # NOTE: if I lock/unlock the database that we are importing into ($k),
    # and it is a brand new, empty database, File::KDBX throws an exeption.
    # Until/unless that is fixed, this code seems to work OK.
    # https://github.com/chazmcgarvey/File-KDBX/issues/4
    # I'm a tad concerned that no fields are protected in this situation...
    my $txn = $new_group->begin_work( entries=>1, groups=>1, history=>1)
						if (ref($iKDB) eq 'File::KDBX');
    $iKDB->unlock(); # Unlock the inbound DB file
    $k->unlock() if (ref($k) eq 'File::KeePass'); # See note just above
    # Copy the $iKDB into our $k at $new_group
    foreach my $i_root_grp (@root_groups) {
      copy_kdb_group_tree($k,$i_root_grp,$new_group);
    }
    $k->lock()           if (ref($k) eq 'File::KeePass');
    $new_group->commit() if (ref($k) eq 'File::KDBX');;
    $iKDB->lock(); # Really not needed since we close it momentarily...
  }

  # Close the $iKDB
  $iKDB->clear() if (ref($iKDB) eq 'File::KeePass');
  $iKDB->reset() if (ref($iKDB) eq 'File::KDBX');
  $iKDB=undef;

  # Refresh all paths and mark state as changed
  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();
}

sub import_KDBX4_KeePassXC {
  my $file = shift @_;
  my $master_pass = shift @_;
  my $key_file = shift @_;
  my $grp_name = shift @_;
  my $parent_group = shift @_;
  our $state;

  # This requires KeePassXC so notify the user if we don't have it
  my $can_kpxc = can_kpxc($opts->{kpxcexe}, $KPXC_MIN_VER);
  if (! $can_kpxc) {
    print color('yellow') .
      "To import KDBX4 files, one of these is required:\n" .
      " - Recommended Perl module File::KDBX, or\n" .
      " - KeePassXC $KPXC_MIN_VER or newer.\n" .
      color('clear') .
      "For KeePassXC, you must specify the full path to the KeePassXC\n" .
      "program using the --kpxcexe commmand line parameter. Provide the\n" .
      "path to the keepassxc-cli command or to a KeePassXC AppImage binary.\n" .
      " - https://keepassxc.org/download/\n".
      "";
    return -1;
  }

  # This requires Expect so try to load it if we don't have it.
  # https://metacpan.org/pod/Expect / libexpect-perl
  if  (! is_loaded('Expect')) {
    runtime_load_module(\%OPTIONAL_PM,'Expect',[qw()]);
  }
  if (! is_loaded('Expect')) {
    print "Perl module Expect is required for this functionality.\n";
    return -1;
  }

  # Gather the KDBX4 file's entries into the $ents hash
  my $timeout = 3; # seconds
  my $ents = gather_kdbx4_entries_KeePassXC($file,$master_pass,$key_file,$timeout);
  if (! defined($ents)) {
    print "The import failed via $opts->{kpxcexe}.\n";
    return -1;
  }
  if (ref($ents) ne 'HASH') {
    print "The import failed with error:\n$ents\n";
    return -1;
  }

  # Add the new group, to its parent or to root if $parent_group==undef
  my $k=$state->{kdb};
  my $top_imp_grp = addGroup($k,$parent_group,{title => $grp_name});

  # Add all of the entities from the import
  my %new_grps = ();
  foreach my $full_path (sort keys (%{$ents})) {
    my ($name,$path,$suffix) = fileparse($full_path);
    $path =~ s%/+$%%;
    # Ensure all that groups exist to put this $ent into
    my @path_parts = File::Spec->splitdir($path);
    for my $i (0..$#path_parts) {
      my $new_path = File::Spec->catdir(@path_parts[0..$i]);
      if (!defined($new_grps{$new_path})) {
        if ($i == 0) {
          $new_grps{$new_path} = addGroup($k,$top_imp_grp,{title => $new_path});
        } elsif ($i > 0) {
          my ($dir_name,$p_path,$suffix) = fileparse($new_path);
          $p_path =~ s%/+$%%;
          $new_grps{$new_path} = addGroup($k,$new_grps{$p_path},{title => $dir_name});
        }
      }
    }
    # Now add the entity.
    # NOTE: Adding ->{id}, ->{group}, ->{title} is not OK for File::KDBX,
    #       but if kpcli had access to File::KDBX it would not be using
    #       KeePassXC to import a KDBX4 file, and so this is OK...
    my %new_ent = ();
    $new_ent{id} = int(rand(1000000000000000)); # A random new id
    $new_ent{group} = $new_grps{$path};
    $new_ent{title} = $name;
    # Loop over fields to add (uname, passwd, etc.)
    my $h = { # KeePassXC to File::KeePass key map
        username => 'UserName',
        password => 'Password',
        url      => 'URL',
        comment  => 'Notes',
        };
    foreach my $k (sort keys %{$h}) {
      $new_ent{$k} = $ents->{$full_path}->{$h->{$k}};
    }
    # Place the new entity into our file
    $k->unlock;
    $k->add_entry(\%new_ent);
    $k->lock;
  }

  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();
}

# Use Expect and "keepassxc cli" to gather the data from a kdbx4 file
# NOTE: As of 07/18/2022, the Expect module does not work on
# MS Windows except for within Cygwin. This code should work
# if that ever changes, but for now, only Cygwin users benefit.
sub gather_kdbx4_entries_KeePassXC {
  my $kdbx_file = shift @_ || undef;
  my $kdbx_pass = shift @_ || undef;
  my $kdbx_keyf = shift @_ || undef;
  my $timeout = shift @_ || 3;
  my $patidx;

  my @kpxc_opts = ();
  # If not keepassxc-cli (like an AppImage), "cli" is needed.
  if ($opts->{kpxcexe} !~ m/-cli([.]exe)$/i) {
    push @kpxc_opts, 'cli';
  }
  # Always need "open" (that's what we're doing.
  push @kpxc_opts, 'open';
  # Determine if we need --no-password or not
  my $expect_pword = 1;
  if (not (defined($kdbx_pass) && length($kdbx_pass) > 1)) {
    push(@kpxc_opts, '--no-password');
    $expect_pword = 0;
  }
  # Determine if we need --key-file= or not
  if (defined($kdbx_keyf) && length($kdbx_keyf) > 0) {
    push(@kpxc_opts, "--key-file=$kdbx_keyf");
  }

  my $exp = Expect->new;
  $exp->log_stdout(0);  # Else everything echos
  #$exp->notransfer(1);
  #$exp->exp_internal(1);
  #$exp->log_file("./expect.log");
  #$exp->raw_pty(1);
  $exp->spawn($opts->{kpxcexe}, @kpxc_opts, $kdbx_file)
	or return "Cannot spawn $opts->{kpxcexe}: $!\n";

  # Use Expect to provide the password at the prompt
  if ($expect_pword) {
    my $prompt = "Enter password to unlock $kdbx_file:";
    $patidx = $exp->expect($timeout, '-re', '^'.$prompt);
    if (! defined($patidx)) { return undef; } # Failed to see password prompt
    $exp->send($kdbx_pass."\n");
    $exp->clear_accum();
  }

  my $prompt = '[^>]+>\s+';
  $patidx = $exp->expect($timeout, '-re', '^'.$prompt);
  if (! defined($patidx)) {
    my $errmsg = $exp->before();
    $errmsg =~ s/\r//g;
    if ($errmsg =~ m/error /i) { return $errmsg; }
    return undef;
  }
  $prompt = $exp->match();
  $prompt =~ s/^[\r\n]+//g;
  $prompt =~ s/[\r\n]+$//g;
  $exp->set_accum('');

  # Complete ls of the entire database
  my @ls_lines = ();
  {
    my $ls_cmd = "ls -R -f\n";
    $exp->send($ls_cmd);
    $patidx = $exp->expect($timeout, '-re', '^'.$prompt);
    my $ls_results = $exp->before();
    $ls_results =~ tr/\r//d;
    @ls_lines = split( "\n", $ls_results );
    if ($ls_cmd =~ m/^$ls_lines[0]\s*$/) {
      shift @ls_lines;
    }
    #print Dumper(\@ls_lines) . "\n";
  }

  my @groups = sort grep(m%/$%, @ls_lines);
  my @entries = sort grep(m%[^/]$%, @ls_lines);
  @entries = sort grep(! m%/[[]empty[]]$%, @entries); # Remove empty folders
  #print Dumper(\@groups, \@entries) . "\n";

  my %ents = ();
  foreach my $entry (@entries) {
    my $show_cmd = "show --show-protected --show-attachments \"$entry\"\n";
    $exp->send($show_cmd);
    $patidx = $exp->expect($timeout, '-re', '^'.$prompt);
    my $show_results = $exp->before();
    $show_results =~ tr/\r//d;
    my @show_lines = split( "\n", $show_results );
    if ($show_cmd =~ m/^$show_lines[0]\s*$/) {
      shift @show_lines;
    }
    my $ent = {};
    my $last_k = undef;
    LINE: foreach my $line (@show_lines) {
      if ($line =~ m/^\w+:/) {
        my ($k, $v) = split(/:\s*/, $line, 2);
        $ent->{$k} = $v;
        $last_k = $k;
      } else {
        if ($last_k eq 'Notes' && $line =~ m/No attachments present\./) {next LINE;}
        $ent->{$last_k} .= "\n" . $line;
      }
    }
    $ents{$entry} = $ent;
  }

  # Cleanup entries
  foreach my $entry (@entries) {
    if (defined($ents{$entry}->{Notes})) {
      $ents{$entry}->{Notes} =~ s/[\r\n]+$//;
    }
    if (defined($ents{$entry}->{Attachments})) {
      my @atts = grep(!/^$/, split(/[\r\n]+/, $ents{$entry}->{Attachments}));
      @atts = map { $_ =~ s/^\s*//; $_; } @atts;
      foreach my $i (0..$#atts) {
        # 'power_outages.txt (1.2 KiB)'
        if ($atts[$i] =~ m/^(.+) [(]([^)]+)[)]$/) {
          $atts[$i] = {name => $1, size => $2};
        }
      }
      $ents{$entry}->{Attachments} = \@atts;
    }
  }
  #print Dumper(\%ents) . "\n";

  # Gather attachements
  foreach my $entry (@entries) {
    if (defined($ents{$entry}->{Attachments})) {
      foreach my $att (@{$ents{$entry}->{Attachments}}) {
        my @tmpdir = File::Spec->splitdir(File::Spec->tmpdir());
        my $tmpfile = File::Spec->catfile(@tmpdir, "kpcli-kpxc-$$.tmp");
        unlink $tmpfile;
        my $att_cmd = "attachment-export \"$entry\" \"$att->{name}\" \"$tmpfile\"\n";
        #print $att_cmd . "\n";
        $exp->send($att_cmd);
        $patidx = $exp->expect($timeout, '-re', '^'.$prompt);
        my $att_results = $exp->before();
        if (-f -r $tmpfile) {
          my $data = slurp_read_file($tmpfile);
          unlink $tmpfile;
          $att->{data} = $data;
        }
        #print "$att_results\n";
      }
    }
  }
  #print Dumper(\%ents) . "\n";

  # Exit from keepassxc-cli
  $exp->send( "quit\n" );
  $exp->soft_close();

  return (\%ents);
}

sub cli_reroot($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  my $k = $state->{kdb};
  if (ref($k) ne 'File::KDBX') {
    print "This command is only relevant to KDBX4 database files.\n";
    return -1;
  }

  my $raw_pathstr = $params->{args}->[0];
  my $grp_path = normalize_path_string($raw_pathstr);
  if (! defined($state->{all_grp_paths_fwd}->{$grp_path})) {
    print "Path does not exist: /" . humanize_path($grp_path) . "\n";
    return -1;
  }

  my $grp = get_group_by_uuid($k, $state->{all_grp_paths_fwd}->{$grp_path});
  if (getID($k->root) eq getID($grp)) {
    print "That group is already the root group...\n";
    return -1;
  }

  print "\n";
  print "CAUTION: all data outside of the new root group will be lost.\n";
  print "Confirm if you would you like to do this? [y/N] ";
  my $key=get_single_key();
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  print "\n";
  if (lc($key) ne 'y') {
    print "Operation canceled.\n";
    return;
  }

  $k->root($grp); # Do the re-root

  # Refresh all paths and mark state as changed
  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();

  # cd to the new KDBX4 root since that's the normal starting point
  my $root_name = getLabel($state->{kdb}->root, 1); # Don't want utf8
  cli_cd($term, {'args' => ["/$root_name"]});
}

sub cli_passwd() {
  our $state;

  # We don't allow passwd on newly-created, unsaved databases
  if (! defined($state->{kdb_file})) {
    print "Please use saveas to save newly created databases.\n";
    return -1;
  }

  print "Changing password for ".$state->{kdb_file}."\n";

  # Ask for the current password if it exists
  if (defined($state->{master_pass})) {
    my $test_passwd = GetMasterPasswd("The current password: ");
    my $curr_passwd = $state->{get_master_passwd}();
    if ($test_passwd ne $curr_passwd) {
      print "Incorrect password.\n";
      return -1;
    }
  }

  # Get the new password from the user with double entry verification
  my $master_pass=GetMasterPasswdDoubleEntryVerify("The new password: ");
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  if (! defined($master_pass)) { return undef; }

  # Set the new password and the kdb_has_changed flag, then ask the
  # user if they want to save the database now.
  $state->{put_master_passwd}($master_pass);
  $state->{kdb_has_changed}=1;
  print "Password changed but file not saved. Save it now? [y/N]";
  my $key=get_single_key();
  print "\n";
  if (lc($key) ne 'y') { return 0; }
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  return cli_save(undef);
}

# Exports (parts of) the currently opened database to a new file.
# It only uses File::KeePass and so can only write KBDv1 and KDBX3 files.
# That may change in the future, and won't be terribly difficult, but for
# now this is an intentional design decision to avoid the additional user
# prompting around KDBX3 vs KDBX4. Most any program that supports KDBX4
# will be able to import a KDBX3 file...
sub cli_export($$) {
  my $file=shift @_;
  my $key_file=shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # Warn is we are being asked to overwrite a file
  if (-e $file) {
    print "WARNING: $file already exists.\n" .
		"Overwrite it? [y/N] ";
    my $key=get_single_key();
    print "\n";
    if (lc($key) ne 'y') {
      return -1;
    }
  }

  # Ask if the key file should be generated, if it doesn't exist
  my $make_keyfile=0;
  if (defined($key_file) && (! -f $key_file)) {
    print "Your specified key file does not exist. Generate it? [y/N] ";
    my $key=get_single_key();
    print "\n";
    if (lc($key) ne 'y') {
      return -1;
    }
    $make_keyfile=1;
    if (recent_sigint()) { return undef; } # Bail on SIGINT
  }

  # Get the master password for the exported file
  my $master_pass=GetMasterPasswdDoubleEntryVerify();
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  if (! defined($master_pass)) { return undef; }

  # Generate the key file if so instructed
  if (defined($key_file) && $make_keyfile) {
    my $fh=new FileHandle;
    if (! open($fh,'>',$key_file)) {
      print "ERROR: Could not open key file for writing: $key_file\n";
      return -1;
    }
    my $KEYFILE_SIZE = 2048;
    print $fh generateKeyfileContents($KEYFILE_SIZE);
    close($fh);
    my $size = (stat($key_file))[7];
    if ($size != $KEYFILE_SIZE) {
      print "ERROR: generated key file is the wrong size: $key_file\n";
      return -1;
    }
  }

  # Only allow an empty password if a reasonable $key_file exists
  if (length($master_pass) == 0 && ( ! -e $key_file || -s $key_file < 128 )) {
    print	"For your safety, empty passwords are not allowed\n" .
		"with key files less than 128 bytes in length...\n";
    return;
  }

  # Build the new kdb in RAM
  my $new_kdb=new File::KeePass;
  {
    my $k=$state->{kdb};
    $k->unlock(); # Required so that we can copy the passwords

    my @root_groups = ();
    if (get_pwd() ne '/') {
      # Grab the root group's $id at our pwd
      my $pwd_group_id = $state->{path}->{id};
      $root_groups[0] = get_group_by_uuid($k, $pwd_group_id);
    } else {
      @root_groups = get_root_groups($k);
    }

    # Put all of the root groups into the new file (entire file copy)
    foreach my $root_grp (@root_groups) {
      copy_kdb_group_tree($new_kdb,$root_grp,undef);
    }

    $k->lock(); # Relock
  }

  # File::KeePass defaults to v1 (*.kdb) and if the user is asking
  # to export to v2 (*.kdbx) we need to override that default.
  if ($file =~ m/[.]kdbx$/) {
    $new_kdb->{header}->{version} = 2;
  }

  # Generate the new kdb/kdbx file into the $new_db_bin variable
  $new_kdb->unlock;
  my $new_db_bin=$new_kdb->gen_db(composite_master_pass('File::KeePass', $master_pass,$key_file));
  $new_kdb->lock;

  # Test parsing the kdb from RAM (we'll most likely die if this fails)
  my $new_db=new File::KeePass;
  $new_db->parse_db($new_db_bin,composite_master_pass('File::KeePass', $master_pass,$key_file));

  # Now write the new kdb to disk
  my $fh=new FileHandle;
  if (open($fh,'>',$file)) {
    print $fh $new_db_bin;
    close $fh;
    my $v = $new_db->{header}->{version};
    my @db_types = (
        { name => 'KDBv1', },
        { name => 'KDBX3', },
	);
    my $i = $v - 1;
    my $ver = "v$v ($db_types[$i]->{name})";
    print "Exported KeePass $ver format to $file\n";
  } else {
    print "Could not open \"$file\" for writing.\n";
  }

  return 0;
}

# A helper function for cli_export() and cli_import(). It takes a kdb object,
# a group as a starting point to copy from, and optionally a parent_group to
# copy to. It copies everything from the source group's root downward. In our
# use cases, the _target_ $kdb object passed in here is typically a different
# one than the _source_ $group is from.
sub copy_kdb_group_tree {
  my $kdb=shift @_;
  my $group=shift @_;
  my $parent_group=shift @_ || undef; # When undef, it writes to the root

  # Add the new group, to it's parent or root if $parent_group==undef
  my $new_group = addGroup($kdb,$parent_group,
	{
	title => getLabel($group),
	icon => $group->{icon},
	id => getID($group),
	group => $parent_group,
	});

  # Add the new_group's entries
  if (ref($group->{entries}) eq 'ARRAY') {
    foreach my $entry (@{$group->{entries}}) {
      my $ent_hash = entry_as_hash($entry);
      if (ref($kdb) eq 'File::KeePass') {
        $ent_hash->{group} = $new_group;
        $kdb->add_entry($ent_hash);
      } elsif (ref($kdb) eq 'File::KDBX') {
        delete($ent_hash->{id}); # Should not exist (code not needed)
        my $parent_grp = undef;
        if (ref($new_group) eq 'File::KDBX::Group') {
          $parent_grp = $new_group;
        } else {
          $parent_grp = get_group_by_uuid($kdb, $new_group);
        }
        if (defined($parent_grp)) {
          my $new_ent = $parent_grp->add_entry({label => $ent_hash->{title}});
          update_entry($kdb, $new_ent, $ent_hash);
          #print "LHHDcptree: grp=".$parent_grp->label.", ent=$ent_hash->{title}\n";
        }
      } else {
        warn "copy_kdb_group_tree() called with unworkable KeePass module!\n";
      }
    }
  }

  # Add the new_group's child groups
  if (ref($group->{groups}) eq 'ARRAY') {
    foreach my $child_grp (@{$group->{groups}}) {
      copy_kdb_group_tree($kdb,$child_grp,$new_group);
    }
  }
}

sub cli_saveas($) {
  my $file=shift @_;
  my $key_file=shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # If we're using File::KeePass and the user asked for a *.kdbx file,
  # check the File::KeePass version for sufficiency.
  if (ref($state->{kdb}) eq 'File::KeePass' &&
           version->parse($File::KeePass::VERSION) < version->parse('2.03') &&
           $file =~ m/\.kdbx$/i) {
    print "KeePass v2 (*.kdbx files) require File::KeePass >= v2.03\n";
    return;
  } elsif (ref($state->{kdb}) eq 'File::KDBX' && $file =~ m/\.kdb$/i) {
    print color('yellow').
          "It is not possible to downgrade a KDBX4 file to KDBv1.\n".
          color('clear').
          "If you really want to, you can create a new KDBv1 file\n".
          "(newdb command) and then import your KDBX4 file into it,\n".
          "possibly suffering some data loss.\n";
    return;
  }

  # Warn if we are being asked to overwrite a file
  if (-e $file) {
    print "WARNING: $file already exists.\n" .
                "Overwrite it? [y/N] ";
    my $key=get_single_key();
    print "\n";
    if (lc($key) ne 'y') {
      return -1;
    }
    if (recent_sigint()) { return undef; } # Bail on SIGINT
  }

  # Ask if the key file should be generated, if it doesn't exist
  my $make_keyfile=0;
  if (defined($key_file) && (! -f $key_file)) {
    print "Your specified key file does not exist. Generate it? [y/N] ";
    my $key=get_single_key();
    print "\n";
    if (lc($key) ne 'y') {
      return -1;
    }
    $make_keyfile=1;
    if (recent_sigint()) { return undef; } # Bail on SIGINT
  }

  # Get the master password for the file
  my $master_pass=GetMasterPasswdDoubleEntryVerify();
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  if (! defined($master_pass)) { return undef; }

  # Generate the key file if so instructed
  if (defined($key_file) && $make_keyfile) {
    my $fh=new FileHandle;
    if (! open($fh,'>',$key_file)) {
      print "ERROR: Could not open key file for writing: $key_file\n";
      return -1;
    }
    my $KEYFILE_SIZE = 2048;
    print $fh generateKeyfileContents($KEYFILE_SIZE);
    close($fh);
    my $size = (stat($key_file))[7];
    if ($size != $KEYFILE_SIZE) {
      print "ERROR: generated key file is the wrong size: $key_file\n";
      return -1;
    }
  }

  # Only allow an empty password if a reasonable $key_file exists
  if (length($master_pass) == 0 &&
	! ( defined($key_file) && -e $key_file && -s $key_file >= 128 )) {
    print	"For your safety, empty passwords are not allowed\n" .
		"with key files less than 128 bytes in length...\n";
    return;
  }

  destroy_found();  # Remove /_found dir if it exists
  utf8_change_strings_KDBv1($state, 'encode'); # Encode to bytestring
  my $k = $state->{kdb}; # For brevity below
  $k->unlock;
  if (ref($k) eq 'File::KeePass') {
    my $comp_mp = composite_master_pass('File::KeePass', $master_pass,$key_file);
    scrub_unknown_values_from_all_groups(); # TODO - remove later
    $k->save_db($file, $comp_mp);
  } elsif (ref($k) eq 'File::KDBX') {
    my $comp_mp = composite_master_pass('File::KDBX', $master_pass,$key_file);
    $k->dump_file($file, $comp_mp);
  } else {
    print "Please report this bug in the saveas command!\n";
    return -1;
  }
  $k->lock;

  # Properly close and remove lock file before the reopen below.
  # This snipped of code was copied from sub cli_close.
  $state->{'kdb'}->clear() if (ref($state->{kdb}) eq 'File::KeePass');
  $state->{'kdb'}->reset() if (ref($state->{kdb}) eq 'File::KDBX');
  new_kdb($state); # Note, this removes the old *.lock file
  if (defined($state->{kdb_file_handle})) {
    close $state->{kdb_file_handle};
  }

  # Open the newly created, saveas-ed file.
  my $err = open_kdb($file, $key_file, $master_pass); # Sets $state->{'kdb'}
  if (length($err)) {
    print "Error re-opening saved file: $err\n";
  } else {
    my $ftype = '*type unknown*';
    if (defined($state->{kdbx_ver})) {
      $ftype = 'KDBX v'.$state->{kdbx_ver};
    } elsif ($state->{kdb_ver}) {
      $ftype = 'KDB v'.$state->{kdb_ver};
    }
    print "You are now operating on a $ftype file: $file\n";
  }

  return 0;
}

# This routine takes a raw (directly from user input) path string
# and "normalizes" it (converts it to NULL-separated w/out escapes)
# and splits it into its dirname and basename components.
sub normalize_and_split_raw_path($) {
  my $raw_pathstr=shift @_;

  my $path = normalize_path_string($raw_pathstr);

  my $basename='';
  if ($path =~ m/\0/) {			# case of at least one path delimeter
    $path =~ s/\0([^\0]+)$//;
    $basename=$1;
  } elsif ($raw_pathstr =~ m/^\//) {	# case of simple "/foo" (no subdir)
    $basename=$path;
    $path='';
  } else {				# case of simple "foo" (no path delims)
    $path = normalize_path_string(get_pwd());
    $basename=$raw_pathstr;
  }
return($path,$basename);
}

sub cli_rmdir($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $raw_pathstr=$params->{'args'}->[0];
  my $grp_path = normalize_path_string($raw_pathstr);
  if (! defined($state->{all_grp_paths_fwd}->{$grp_path})) {
    print "Path does not exist: /" . humanize_path($grp_path) . "\n";
    return -1;
  }

  my $group_to_del_id = $state->{all_grp_paths_fwd}->{$grp_path};
  my $group_to_del = get_group_by_uuid($state->{kdb}, $group_to_del_id);

  # Can't remove the root group from a KDBX4 file
  if (ref($state->{kdb}) eq 'File::KDBX') {
    if ($group_to_del->is_root) {
      print "Cannot remove the root group of a KDBX4+ format file.\n";
      return -1;
    }
    if ($group_to_del->is_recycle_bin) {
      print "Cannot remove the Recycle Bin of a KDBX4+ format file.\n";
      return -1;
    }
  }

  # Count the entries and groups below this group and warn if >0
  my @entries = ();
  my $entry_cnt=0;
  if (defined($group_to_del->{entries})) {
    @entries = grep(m/^\Q$grp_path\E\0/,keys %{$state->{all_ent_paths_fwd}});
    $entry_cnt = scalar(@entries);
  }
  my $group_cnt=0;
  if (defined($group_to_del->{entries})) {
    $group_cnt=
	scalar(grep(m/^\Q$grp_path\E\0/,keys %{$state->{all_grp_paths_fwd}}));
  }
  my $child_cnt=$entry_cnt + $group_cnt;
  if ( $child_cnt > 0) {
    print "WARNING: This group has $child_cnt child groups and/or entries.\n" .
	"Really remove it!? [y/N] ";
    my $key=get_single_key();
    print "\n";
    if (lc($key) ne 'y') {
      return -1;
    }
  }

  # Recycle any entries that we're also removing
  if ($entry_cnt > 0) {
    if (! (defined($opts->{'no-recycle'}) && int($opts->{'no-recycle'}))) {
      foreach my $ent_path (@entries) {
        my $ent_id = $state->{all_ent_paths_fwd}->{$ent_path};
        my $ent = get_entry_by_uuid($state->{kdb}, $ent_id);
        my $errmsg = recycle_entry($state, $ent);
        if (defined($errmsg)) { print "WARNING: $errmsg\n"; }
      }
    }
  }

  # Delete the group, refresh our state paths, request save, etc.
  if (ref($state->{kdb}) eq 'File::KDBX') {
    my $deleted_group = $group_to_del->remove;
  } elsif (ref($state->{kdb}) eq 'File::KeePass') {
    my $deleted_group = $state->{kdb}->delete_group({ id => $group_to_del_id });
  }

  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();
  return 0;
}

sub get_parent_group_of_uuid {
  my $kdb = shift @_;
  my $uuid = shift @_;

  # Most of the time, this top code will work and return the
  # information. If/when it might get called prior to the
  # all_(ent|grp)_paths being built, alternatives are below.
  my $obj_path = undef;
  if (defined($state->{all_ent_paths_rev}->{$uuid})) {
    $obj_path = $state->{all_ent_paths_rev}->{$uuid};
  } elsif (defined($state->{all_grp_paths_rev}->{$uuid})) {
    $obj_path = $state->{all_grp_paths_rev}->{$uuid};
  }
  if (defined($obj_path)) {
    my @obj_path = split("\0", $obj_path);
    pop @obj_path;
    my $pgroup_path = join("\0", @obj_path);
    my $pgroup_uuid = $state->{all_grp_paths_fwd}->{$pgroup_path};
    my $pgrp = get_group_by_uuid($kdb, $pgroup_uuid);
    return $pgrp;
  }

  my $this_obj = getObjByID($uuid);
  if (! defined($this_obj)) {
    warn "get_parent_group_of_uuid() did not find an obj for the UUID!\n";
    return undef;
  }
  if (ref($kdb) eq 'File::KDBX') {
    my $lineage = $this_obj->lineage();
    my $parent_group = $lineage->[scalar(@{$lineage}) - 1];
    return $parent_group;
  } elsif (ref($kdb) eq 'File::KeePass') {
    if (defined($this_obj) && defined($this_obj->{group})) {
      my $pgrp = get_group_by_uuid($kdb, $this_obj->{group});
      return $pgrp;
    }
  } else {
    warn "get_parent_group_of_uuid() can't handle \$kdb it was given!\n";
  }
  return undef;
}

sub cli_mkdir($) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || deny_if_readonly() || warn_if_file_changed()) {
    return;
  }

  my $raw_pathstr = $params->{args}->[0];
  my ($path,$newdir) = normalize_and_split_raw_path($raw_pathstr);

  # Make sure the group doesn't already exist.
  my $newdir_path="$path\0$newdir";
  $newdir_path=~s/^\0+//;
  if (defined($state->{all_grp_paths_fwd}->{$newdir_path})) {
    print "Path already exists: /" . humanize_path($newdir_path) . "\n";
    return -1;
  }

  $newdir = decode_if_not_utf8($newdir); # Input from Term::ShellUI

  # Create the group
  my $group='';
  if ($path eq '') {
    if (ref($state->{kdb}) eq 'File::KDBX' ||
	(defined($state->{kdbx_ver}) && $state->{kdbx_ver} >= 4.0) ) {
      print "KDBX4+ file formats only allows for a single root-level group.\n" .
            "This file's root group is: /" .$state->{kdb}->root->name."\n";
      return -1;
    }
    # For root level group, parent_group = undef.
    $group = addGroup($state->{kdb},undef,{title => $newdir});
  } elsif (defined($state->{all_grp_paths_fwd}->{$path})) {
    my $group_id=$state->{all_grp_paths_fwd}->{$path};
    $group = addGroup($state->{kdb},$group_id,{title => $newdir});
  } else {
    print "Cannot make directory at path " . humanize_path($path) . "\n";
    return -1;
  }

  # Because we created a new group we need to refresh ours state paths
  refresh_state_all_paths();
  $state->{kdb_has_changed}=1;
  RequestSaveOnDBChange();
  return 0;
}

sub humanize_path {
  my $path=shift @_;
  my $decode_utf8 = shift @_ // 1; # By default, decode to utf8
  $path =~ s/\//\\\//g;
  $path =~ s/\0/\//g;
  # The $path given to this function is always from the NULL separated
  # style from normalize_path() and that is never UTF-8 encoded. Since
  # we are being asked to "humanize" it, we also decode it to UTF-8 as
  # doing so fixes a ton of display bugs for things like error messages.
  # e.g. - print "Unknown entity: " . humanize_path($src_path) . "\n";
  # However, there are some rare cases when we explicitly do not want
  # to decode to UTF-8 and the complete_*() functions are examples.
  $path = decode_if_not_utf8($path) if ($decode_utf8);
  return $path;
}

sub cli_newdb {

  # First ask to save if the currently open DB needs has changes.
  if ($state->{kdb_has_changed}) {
    RequestSaveOnDBChange();
  }

  my @db_types = (
	{
	name => 'KDB',
	module => 'File::KeePass',
	desc => 'The original KeePass format (*.kdb).',
	},
	{
	name => 'KDBX3',
	module => 'File::KeePass',
	desc => 'The first KeePass XML format (*.kdbx v3).',
	},
	{
	name => 'KDBX4',
	module => 'File::KDBX',
	desc => 'The second KeePass XML format (*.kdbx v4).',
	},
	);

  print "Choose your file format:\n\n";
  my @choices = ();
  foreach my $i (0 .. $#db_types) {
     my $dbt = $db_types[$i];
     #printf(" %d. %-s supported using %-s\n", $i+1, $dbt->{name}, $dbt->{module});
     #print  "     - $dbt->{desc}\n";
     printf(" %d. %-5s - %-s\n", $i+1, $dbt->{name},$dbt->{desc});
     printf("            Supported using %-s\n", $dbt->{module});
     push @choices, '('. ($i+1) .')';
  }
  push @choices, '(c)ancel';
  print "Choose: ".join("/",@choices)."? ";
  my $key = get_single_key(); print "$key" if (ord($key) > 32 && ord($key) < 176);
  print "\n";
  if (!($key =~ m/^\d+$/ && $key > 0 && $key <= scalar(@db_types))) {
    return -1;
  }

  my $dbt = $db_types[$key-1];
  if (! is_loaded($dbt->{module})) {
    print $dbt->{module}." is unavailable.".
	" Please install it to use this option.\n";
    return -1;
  }

  if ($dbt->{module} eq 'File::KDBX') {
    my @errs = can_kdbx();
    if (scalar(@errs)) {
      print color('bold yellow') .
	"FAILED: " .
	color('clear') . color('red') .
	"There are problems with File::KDBX, as follows:\n".
	" - ".join("\n - ", @errs)."\n".
	color('clear');
      return -1;
    }
  }

  our $state; # new_kdb populates $state->{kdb}
  new_kdb($state, $dbt->{module});

  # For KDBX3, need to set the version=2
  my $newdb = $state->{kdb};
  if ($key == 2) { # User chose KDBX3
    $newdb->{header}->{version} = 2;
    $state->{kdb_ver} = 2;
    $state->{kdbx_ver} = 3.0;
  }

  print "Done. Use the saveas command to write to disk.\n";
  return 0;
}

sub cli_open {
  my $path=shift @_;
  my $key=shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # If cli_close() does not return 0 the user decided not to close the file
  if (cli_close() != 0) {
    return -1;
  }

  if ( -f $path ) {
    my $err = open_kdb($path, $key);
    if (length($err)) {
      print "Error opening file: $err\n";
    }
  } else {
    print "Cannot open: $path\n";
  }
  print dump_of_all_paths()."\n" if ($DUMP_PATHS_ON_OPEN_AND_MKTESTDB);
}

# Term::ShellUI::complete_onlyfiles does not work properly
# on mswin and so we replace it with a call to our very
# own my_nongnu_complete_files(). Ultimately, we replaced it
# for all platforms because of other nagging bugs discovered.
sub my_complete_onlyfiles {
  my $self = $_[0];
  if (1 || lc($^O) =~ m/^mswin/) {
    my $cmpl = $_[1];
    my $path = $cmpl->{tokens}->[$cmpl->{tokno}];
    if (length($path) > $cmpl->{tokoff}) {
      $path = substr($path, 0, $cmpl->{tokoff});
    }
    my @dir_contents = my_nongnu_complete_files($path, undef, undef, $self);
    return \@dir_contents;
  }
  return &Term::ShellUI::complete_onlyfiles(@_);
}

# Get a single keypress from the user
sub get_single_key {
  my $drain_first = shift @_ || 1;
  our $state;
  my $key='';
  $|=1; # Needed to flush STDOUT on Windows cmd prior to calling ReadMode
  ReadMode('raw'); # Turn off controls keys
  while($drain_first && defined( $key = ReadKey(-1) ) ) {} # Drain STDIN first
  while (not defined ($key = ReadKey(-1))) {
    # If the user hit ^C (SIGINT) then we need to stop
    if (recent_sigint()) { return undef; }
    # No key yet, but let's not eat 100% CPU while waiting, so sleep.
    Time::HiRes::sleep(0.1);
  }
  ReadMode('restore');
return $key;
}
# Get a single line of input from the user
sub get_single_line {
  our $state;
  $|=1; # Needed to flush STDOUT on Windows cmd prior to calling ReadMode
  my $input='';
  while (1) {
    my $c  = get_single_key(0);
    if (ord($c) == 3) { # ^C
      return '';
    } elsif (ord($c) == 127 || ord($c) == 8) { # backspace (Linux/Windows)
      if (length($input) > 0) {
        $input = substr($input,0,length($input) - 1);
        print chr(8)." ".chr(8); # Erase a character
      }
    } elsif ($c =~ m/[\n\r]/) {
      return $input;
    } else {
      $input.=$c;
      print $c;
    }
  }
}

sub cli_close {
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  if ($state->{kdb_has_changed}) {
    print "WARNING: The database has changed and was not saved.\n" .
	"Really close it? [y/N] ";
    my $key=get_single_key();
    print "$key\n";
    if (lc($key) ne 'y') {
      return -1;
    }
  }

  if (ref($state->{'kdb'}) eq 'File::KeePass') {
    $state->{'kdb'}->clear();
  } elsif (ref($state->{'kdb'}) eq 'File::KDBX') {
    $state->{'kdb'}->reset();
  }

  new_kdb($state); # Note, this removes the old *.lock file
  if (defined($state->{kdb_file_handle})) {
    close $state->{kdb_file_handle};
  }
  return 0;
}

# This sets $state to a brand new, empty, unsaved database
sub new_kdb {
  my $state = shift @_;
  my $new_style = shift @_ || undef;
  $state->{kdb_has_changed}=0;

  if (! defined($new_style)) {
    # TODO - in the "! defined()" case, we are defaulting to File::KeePass,
    # and so running kpcli without a file to open will start a 1.x db file.
    # This maybe needs to be influenced by a command line parameter, or by
    # the availability of File::KDBX (if we'd like to default to KDBX4).
    if (! defined($state->{'kdb'})) {
      $new_style = 'File::KeePass';
    } elsif (ref($state->{'kdb'}) eq 'File::KeePass') {
      $new_style = 'File::KeePass';
    } elsif (ref($state->{'kdb'}) eq 'File::KDBX') {
      $new_style = 'File::KDBX';
    }
  }

  if ($new_style eq 'File::KeePass') {
    $state->{'kdb'} = File::KeePass->new;
    #$state->{kdb_ver} = $state->{kdb}->{header}->{version}; # undef after ->new()
    $state->{kdb_ver} = 1; # Only provide 1.x (*.kdb) features by default
    $state->{kdbx_ver} = undef;
    $state->{kdbv1_utf8_is_decoded} = 0; # This new DB hasn't been decoded
    # To be compatible with KeePassX
    addGroup($state->{kdb},undef,{title => 'eMail'});
    addGroup($state->{kdb},undef,{title => 'Internet'});
  } elsif ($new_style eq 'File::KDBX') {
    $state->{'kdb'} = File::KDBX->new;
    # Defaults to 3.1. See github.com/chazmcgarvey/File-KDBX/issues/5
    #$state->{kdbx_ver} = 4.0;
    #$state->{'kdb'}->version(KDBX_VERSION_4_0());
    $state->{kdbx_ver} = 4.1;
    $state->{'kdb'}->version(KDBX_VERSION_4_1());
    # See https://github.com/chazmcgarvey/File-KDBX/issues/6
    $state->{'kdb'}->kdf_parameters({
	KDF_PARAM_UUID() => KDF_UUID_ARGON2D(),
	KDF_PARAM_ARGON2_ITERATIONS() => KDF_DEFAULT_ARGON2_ITERATIONS(),
	KDF_PARAM_ARGON2_MEMORY() => KDF_DEFAULT_ARGON2_MEMORY(),
	KDF_PARAM_ARGON2_PARALLELISM() => KDF_DEFAULT_ARGON2_PARALLELISM(),
	KDF_PARAM_ARGON2_VERSION() => KDF_DEFAULT_ARGON2_VERSION(),
    });
  } else {
    die "Cannot make a \"$new_style\" styled database!\n";
  }

  refresh_state_all_paths();
  if (defined($state->{placed_lock_file}) && -f $state->{placed_lock_file}) {
    unlink($state->{placed_lock_file});
  }
  delete($state->{placed_lock_file});
  delete($state->{kdb_file});
  delete($state->{key_file});
  delete($state->{master_pass});
  cli_cd($term, {'args' => ["/"]});
}

# The mktestdb command was added for v4.1 and proved very helpful in the
# utf8 support that was added then. It simply calls cli_newdb() so that the
# user can choose the type of DB file to make, and then it populates the
# /Root group with a number of entries.
sub cli_mktestdb {
  our $state;

  my $zero_on_success = cli_newdb(); # User chooses the newdb type
  if ($zero_on_success != 0) {
    print "Failed to make a new db. Bailing out of mktestdb...\n";
    return undef;
  }
  my $k = $state->{kdb}; # just for shorter syntax below

  # This subroutine builds groups and entries with UTF-8 characters within
  # them and thus it needs utf8 support in all circumstances. Perl's "local"
  # syntax is very nice here in that it changes the value of global $NO_UTF8,
  # including for called subroutines, only for this function's scope.
  # https://perldoc.perl.org/perlsub#Temporary-Values-via-local()
  my $NO_UTF8orig = $NO_UTF8; # We need the original value later
  local $NO_UTF8 = 0;         # Locally ensure UTF-8 support

  # Everything in a KDBX4 file must go underneath /Root, while that
  # path does not exist in KDB or KDBX3 files by default. And so, we
  # use /Root here for all formats. If this name is to be changed then
  # there would be more work to do here since KDBX4 requires everything
  # to appear under a single root dir (/Root by default).
  my $root_path = '/Root';  # The root group in which to place things
  my $root_normpath = normalize_path_string($root_path);
  my $root_gid = $state->{all_grp_paths_fwd}->{$root_normpath} // undef;

  # If the /$root_path group does not already exist, create it.
  # As long as root_path=Root then this should only be needed
  # for File::KeePass managed databases as KDBX4 has /Root.
  if (! defined($root_gid)) {
    my ($root_title) = $root_path =~ m%^/*([^/]+)$%; # Title is without the /
    print "Adding group '$root_title' to '/'\n";
    my $new_grp = addGroup($state->{kdb},undef,{title => $root_title});
    refresh_state_all_paths();
  }

  # Grab root_gid again since it could be newly created.
  $root_gid = $state->{all_grp_paths_fwd}->{$root_normpath};
  if (! defined($root_gid)) {
    warn "ERROR: Missing root_gid for root_path=$root_path. Bailing out.\n";
    return 0;
  }

  # For convenience, cd the user into /$root_path
  print "Doing: cd $root_path\n";
  cli_cd($term, {'args' => [$root_path]});

  # I have no idea how, but File::KeePass is storing UTF-8 strings in the KDBv1
  # format in a far smaller representation than I can figure out how to by
  # starting with just a perl string, thus the silly shenanigans here with the
  # special assignment of $utf8_test_str... On 04/15/2024, I decided to have
  # this rouine *only* produce UTF-8 entries and so eliminated the need for
  # this junk, but I am leaving it here in case I need to refer to it.
  my $utf8_test_str = 'Général';
#  if (!is_kdb_format_xml($k) && $NO_UTF8) { # Not XML-based
#    $utf8_test_str = "G\351n\351ral"
#  } else {
#    # The next line is just to document how é comes from File::KDBX w/out it.
#    # The \nnn are octal codes.
#    $utf8_test_str = "G\303\251n\303\251ral" if (is_kdb_format_xml($k));
#  }

  # Add some top-level groups to the root_path
  my $size = 2;
  my @top_grps = ();
  foreach my $i (1..$size) {
    push @top_grps, "group-$i";
    push @top_grps, "group-$utf8_test_str-$i";
  }
  my %top_grps = ();
  foreach my $gtitle (@top_grps) {
    # NOTE: This decode_if_not_utf8() is in-line *replacing* the entries
    # in @top_grps, given how this foreach loop is structured!!!
    $gtitle = decode_if_not_utf8($gtitle);
    print "Adding group '$gtitle' to '$root_path'\n";
    $top_grps{$gtitle} = addGroup($k,$root_gid,{title => $gtitle});
    refresh_state_all_paths(); # Likely overkill
  }

  # Add some entries...
  # NOTE: these @ents are all utf8 by default if the @top_grps were already
  # promoted, and they will be if they should be.
  my @ents = @top_grps; map { $_ =~ s/^group-/entry-/; } @ents;
  #print Dumper({g=>\@top_grps, e=> \@ents})."\n";
  my %ents = ();
  # The groups to add the @ents to
  my @grpIDs_for_ents = ($root_gid,
		getID($top_grps{$top_grps[0]}), getID($top_grps{$top_grps[$#top_grps]}));
  ENT_GRP: foreach my $ent_groupID (@grpIDs_for_ents) {
    my $entGrpObj = getObjByID($ent_groupID);
    my $entGrpPath = get_path($entGrpObj);
    foreach my $etitle (@ents) {
      my $title = decode_if_not_utf8($etitle);
      my $new_entry = {
        title => $title,
        group => $ent_groupID,
        strings => {
		'string-1' => 'string-1-value',
		'string-Général-1' => 'string-Général-1-value',
		},
      };
      # strings are not support in KDBv1, so remove them
      if (ref($k) eq 'File::KeePass' && $state->{kdb_ver} == 1) { # KDBv1
        delete($new_entry->{strings});
      }
      # Loop over all the entry fields populating them
      foreach my $key (qw(username url comment password)) {
        my $k2 = decode_if_not_utf8($key);
        $new_entry->{$k2} = "$title-$k2"; # This is a utf8-utf8 pair
        $new_entry->{$k2} .= "\n ... a two-line comment." if ($key eq 'comment');
      }
      # NOTE: the password field is not stored as utf8 in any of the KeePass
      # file formats, but password is in the decode_if_not_utf8() loop just
      # above, for convenience, and then it is undone here, after the loop.
      # This is *not* the same as not making password an utf8 exception in the
      # places where kpcli gets/sets it! Those needs to stay!
      $new_entry->{password} = encode_if_utf8($new_entry->{password});
      foreach my $k (keys %{$new_entry->{strings}}) {
        my $v = $new_entry->{strings}->{$k};
        my $new_k = decode_if_not_utf8($k);
        my $new_v = decode_if_not_utf8($v);
        delete($new_entry->{strings}->{$k});
        $new_entry->{strings}->{$new_k} = $new_v;
      }
      my $ent_group_title = getLabel($new_entry->{group});
      my $entGrpPath_utf8 = decode_if_not_utf8($entGrpPath);
      print "Adding '$new_entry->{title}' to '$entGrpPath_utf8'\n";
      my $new_entry_uuid = addEntry($k,$new_entry);
      if (defined($new_entry_uuid)) {
        $ents{"$entGrpPath/$etitle"} = $new_entry_uuid;
        refresh_state_all_paths(); # Likely overkill
        $state->{kdb_has_changed}=1;
      } else {
        print "Failed to add new entry '$entGrpPath/$etitle'.\n";
      }
    }
  }

  $k->unlock; # Required for both File::KeePass and File::KDBX

  # Everything above was forced into UTF-8 and so we must undo that for KDBv1
  # files before we round-trip a RAM-based DB save/load with File::KeePass.
  utf8_change_strings_KDBv1($state, 'encode', 1); # Force encode to bytestring

  #$DUMP_PATHS_ON_OPEN_AND_MKTESTDB = 1; # To override the global here locally
  print dump_of_all_paths()."\n" if ($DUMP_PATHS_ON_OPEN_AND_MKTESTDB);
  # Now we round-trip through the modules save/load routines so that
  # what we are dealing with includes capturing those code paths.
  my $tmp_rtpasswd = generatePasswordGobbledygook(16); # Grab a random temp password
  my $module = ref($k);
  print "Round-tripping a RAM-based DB save/load through $module...\n";
  if ($module eq 'File::KDBX') {
    my $tmp_enc_data = undef;
    $k->dump_string(\$tmp_enc_data, $tmp_rtpasswd);
    my $new_kdbx = $k->load_string($tmp_enc_data, $tmp_rtpasswd);
    $state->{kdb} = $new_kdbx;
  } elsif ($module eq 'File::KeePass') {
    $k->unlock;
    my $pass_db_string = $k->gen_db($tmp_rtpasswd);
    $k->clear;
    $k->parse_db($pass_db_string, $tmp_rtpasswd);
    $state->{kdb} = $k;
  } else {
    print "Round-tripping in RAM failed. This is likely a BUG!!!\n";
  }

  # If not in NO_UTF8 mode, decode KDBv1 files to UTF8 strings
  if (! $NO_UTF8orig) {
    utf8_change_strings_KDBv1($state, 'decode'); # Decode to utf8
  }

  refresh_state_all_paths();
  $state->{last_ls_ents} = []; # Wipe the ls slate clean

  print dump_of_all_paths()."\n" if ($DUMP_PATHS_ON_OPEN_AND_MKTESTDB);
}

# Used just for debugging. Dumps the non-utf8-encoded "all_*_paths_fwd" values
sub dump_of_all_paths {
  return Dumper( # Intentional Dumper
	{g=>$state->{all_grp_paths_fwd},e=>$state->{all_ent_paths_fwd},}
	);
}

# Answers the question, "is the format of the open database XML or not?"
# which became important when utf8 support was added in April of 2024.
sub is_kdb_format_xml {
  my $k = shift @_;
  my $module_name = ref($k);
  return 1 if ($module_name eq 'File::KDBX');
  return 1 if ($module_name eq 'File::KeePass' && $state->{kdb_ver} > 1);
  return 0 if ($module_name eq 'File::KeePass' && $state->{kdb_ver} == 1);
  warn "ERROR: Bug in is_kdb_format_xml(). Please report it!\n";
  return 0;
}

sub cli_ls {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  $state->{last_ls_ents} = []; # We reload this state in this function

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  my @paths = ();
  if (defined($params) && defined($params->{'args'}) &&
				ref($params->{'args'}) eq 'ARRAY') {
    @paths = @{$params->{'args'}};
  }
  if (scalar(@paths) == 0) { push @paths, get_pwd(); }
  my $paths_count = scalar(@paths);
  my @ent_matches = (); # Collects entries we've been directly asked to list
  my @grp_paths = ();	# Collects groups we've been asked to list
  my $k=$state->{kdb};
  foreach my $path (@paths) {
    my $norm_path = normalize_path_string($path);
    #warn "LHHD: $norm_path\n";
    if (defined($state->{all_grp_paths_fwd}->{$norm_path}) || length($norm_path) < 1) {
      #warn "LHHDx1: $norm_path\n";
      push @grp_paths, $path;
    } elsif (defined($state->{all_ent_paths_fwd}->{$norm_path})) {
      #warn "LHHDx2: $norm_path\n";
      my $tmp_ent = get_entry_by_uuid($k, $state->{all_ent_paths_fwd}->{$norm_path});
      push @ent_matches, $tmp_ent;
    } else {
      #warn "LHHDx3: $norm_path\n";
      my @tmp_ents = shell_expansion($path);
      foreach my $tmp_ent (@tmp_ents) {
        if (defined($state->{all_ent_paths_fwd}->{$tmp_ent})) {
          my $entry_id = $state->{all_ent_paths_fwd}->{$tmp_ent};
          my $ent = get_entry_by_uuid($k, $entry_id);
          push @ent_matches, $ent;
        } elsif (defined($state->{all_grp_paths_fwd}->{$tmp_ent})) {
          push @grp_paths, '/'.humanize_path($tmp_ent);
        }
      }
    }
  }

  my $have_output=0; # Helps manage "\n" placements below.

  # First present the entries that we were directly asked to list
  if (scalar(@ent_matches) > 0) {
    @ent_matches = sort { ncmp(getLabel($a),getLabel($b)); } @ent_matches;
    if ($have_output) { print "\n"; }
    print "=== Entries ===\n";
    print join("\n", @{get_human_entry_list(\@ent_matches, scalar(@{$state->{last_ls_ents}}))}) ."\n";
    push @{$state->{last_ls_ents}}, @ent_matches;
    $have_output++;
  }

  # Now present the groups that we were asked to list
  foreach my $path (sort { ncmp($a,$b) } @grp_paths) {
    my $norm_path = normalize_path_string($path);
    if ($have_output) { print "\n"; }
    if (scalar(@ent_matches) > 0 || scalar(@grp_paths) > 1) {
      # TODO: this use of ALL_USER_INPUT_TO_UTF8 likely can/should be removed,
      # but it's a tad tricky because some of the code paths above can place
      # data into $path that did come from user input (at the command line).
      my $utf8_path = decode_if_not_utf8($path) if ($ALL_USER_INPUT_TO_UTF8);
      print "$utf8_path:\n";
      $have_output++;
    }
    my @groups = (); my @entries = ();
    # Top level ($norm_path eq '')
    if (length($norm_path) < 1) {
      @groups = get_root_groups($state->{kdb});
      @entries = (); # No entries at level 0
    # All other levels than top ($norm_path ne '')
    } else {
      my $group_id = $state->{all_grp_paths_fwd}->{$norm_path};
      # warn "LHHD: $norm_path / $group_id\n";
      my ($grps,$ents) = get_kids_by_group_uuid($state->{kdb},$group_id);
      @groups = sort group_sort @{$grps};
      @entries = sort entry_sort @{$ents};
    }
    # Eliminate "system" entries inside this group that we don't want to show
    my @good_entries = ();
    MATCHES: foreach my $ent (@entries) {
      if (defined($ent) && getLabel($ent) eq 'Meta-Info' && get_username($ent) eq 'SYSTEM') {
        next MATCHES;
      }
      push @good_entries, $ent;
    }
    @entries = @good_entries;
    # Display the groups and entries that we have
    if (scalar(@groups) > 0) {
      print "=== Groups ===\n";
      print join("\n", @{get_human_group_list(\@groups)}) . "\n";
      $have_output++;
    }
    if (scalar(@entries) > 0) {
      print "=== Entries ===\n";
      print join("\n", @{get_human_entry_list(\@entries, scalar(@{$state->{last_ls_ents}}))}) . "\n";
      $have_output++;
      push @{$state->{last_ls_ents}}, @entries;
    }
  }

  return 0;
}

# Returns a full, "humanized" path to the object: /foo/bar/baz
sub get_path($) {
  my $obj = shift @_;

  # NOTE: The method that is used for File::KeePass should also
  #       work for File::KDBX, but I wrote the ->lineage code
  #       first and want to keep it around since it would work
  #       without $state->{all_XXX_paths_rev} being populated.
  if (ref($state->{kdb}) eq 'File::KeePass') {
    my $path = undef;
    my $obj_id = getID($obj);
    EorG: foreach my $e_or_g (qw(all_ent_paths_rev all_grp_paths_rev)) {
      if (defined($state->{$e_or_g}->{$obj_id})) {
        $path = '/' . humanize_path($state->{$e_or_g}->{$obj_id});
        # File::KeePass returns utf8 strings for KDBX3 (XML-based files),
        # and so we have to *always* undo that here if we find those.
        $path = encode_if_utf8($path, 1);
        last EorG;
      }
    }
    return $path;
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    # NOTE: it is important to ask getLabel() to not return utf8 here.
    # This would not be needed if the code above was used instead.
    my $lineage = $obj->lineage;
    my @path_pieces = ();
    foreach my $ent (@{$lineage}) {
      push @path_pieces, getLabel($ent, 1);
    }
    push @path_pieces, getLabel($obj, 1); # The object itself
    my $full_obj_path = '/'.join('/', @path_pieces);
    return $full_obj_path;
  }
}
# Returns the "level" at which the object resides. The "root" is
# level 0, one level down is level 1, etc.
sub get_level($) {
  my $obj = shift @_;
  my $path = get_path($obj);
  my $norm_path = normalize_path_string($path);
  my @pieces = split("\0", $norm_path);
  my $level = $#pieces;
  if (defined($state->{all_ent_paths_fwd}->{$norm_path})) {
    $level--; # For entries, the level is their group's level
  }
  return $level;
}

sub get_group_by_uuid {
  my $kdb = shift @_;
  my $uuid = shift @_;

  if (! (defined($uuid) && length($uuid))) {
    warn "ERROR/BUG: get_group_by_uuid() was given an undef or zero length UUID!\n";
    if ($DO_TRACE_DUMPS) { my $trace = Devel::StackTrace->new; print $trace->as_string; }
    return undef;
  }

  if (ref($kdb) eq 'File::KeePass') {
    my $ent = $kdb->find_group({id=>$uuid});
    return $ent;
  } elsif (ref($kdb) eq 'File::KDBX') {
    my $ents = $kdb->groups->where( uuid => { 'eq' => $uuid, });
    my @entries = @{$ents->to_array()}; # Should have one result (uuid=$uuid)
    if (scalar(@entries) > 1) {
      warn "ERROR/BUG: get_group_by_uuid() has more than one result!\n";
    }
    if (scalar(@entries) < 1) {
      warn "ERROR/BUG: get_group_by_uuid() has fewer than one result!\n";
    }
    my $ent = $entries[0];
    return $ent;
  } else {
    die "get_group_by_uuid() called without a valid kdb object.\n";
  }
  return undef;
}

sub get_entry_by_uuid {
  my $kdb = shift @_;
  my $uuid = shift @_;

  if (ref($kdb) eq 'File::KeePass') {
    my $ent = $kdb->find_entry({id=>$uuid});
    return $ent;
  } elsif (ref($state->{kdb}) eq 'File::KDBX') {
    my $ents = $kdb->entries->where( uuid => { 'eq' => $uuid, });
    my @entries = @{$ents->to_array()}; # Should only have one result (uuid=$uuid)
    if (scalar(@entries) > 1) {
      warn "ERROR/BUG: get_entry_by_uuid)() has more than one result!\n";
    }
    my $ent = $entries[0];
    ##########################################################
    # File::KeePass compatability ############################
    ##########################################################
    # THIS CODE IS PROBLEMATIC AND NEEDS TO BE DONE AWAY WITH!
    ##########################################################
    # With cli_edit, this created a major headache when the
    # "title" didn't appear to be changing. I intend to make
    # sure that I expunge all of cases where we're setting
    # ->{title} for File::KDBX, but it's not done yet.
    ##########################################################
    foreach my $k (qw(title username password url notes)) {
      $ent->{$k} = $ent->$k;
    }
    $ent->{comment} = $ent->notes;
    $ent->{icon} = $ent->icon_id;
    if (defined($ent->{times})) {
      my %map = (
	created => 'creation_time',
	expires => 'expiry_time',
	modified => 'last_modification_time',
	accessed => 'last_access_time',
	);
      foreach my $k (keys %map) {
        # Convert from Time::Piece objects to "YYYY-mm-dd HH:MM:SS"
        # NOTE: File::KDBX accepts this format as valid times.
        if (defined($ent->{times}->{$map{$k}})) {
          if (ref($ent->{times}->{$map{$k}}) eq 'Time::Piece') {
            my $time_piece = $ent->{times}->{$map{$k}};
            $ent->{$k} = $time_piece->strftime("%Y-%m-%d %H:%M:%S");
          } else {
            $ent->{$k} = $ent->{times}->{$map{$k}};
          }
        }
      }
    }
    ##########################################################
    return $ent;
  }
  return undef;
}


# Supports both File::KeePass and File::KDBX
sub get_kids_by_group_uuid {
  my $kdb = shift @_;
  my $grp_uuid = shift @_;

  if (ref($kdb) eq 'File::KeePass') {
    return get_kids_by_group_uuid_KeePass($kdb,$grp_uuid);
  } elsif (ref($kdb) eq 'File::KDBX') {
    return get_kids_by_group_uuid_KDBX($kdb,$grp_uuid);
  } else {
    warn "get_kids_by_group_uuid() called with invalid \$kdb!\n";
  }
  return (undef,undef);
}
# For File::KeePass
sub get_kids_by_group_uuid_KeePass {
  my $kdb = shift @_;
  my $grp_uuid = shift @_;

  my @groups = (); my @entries = ();
  @entries = $kdb->find_entries({group_id=>$grp_uuid});
  @entries = sort entry_sort @entries;
  my $this_grp = $kdb->find_group({id=>$grp_uuid});
  if (defined($this_grp->{groups})) {
    @groups = sort group_sort @{$this_grp->{groups}};
  }
  return (\@groups, \@entries);
}
# For File::KDBX
sub get_kids_by_group_uuid_KDBX {
  my $kdb = shift @_;
  my $grp_uuid = shift @_;

  my $grps = $kdb->groups->where( uuid => { 'eq' => $grp_uuid, });
  my @groups = @{$grps->to_array()}; # Should only have one result (uuid=$grp_uuid)
  if (scalar(@groups) > 1) {
    warn "ERROR/BUG: get_kids_by_group_uuid_KDBX() has more than one result!\n";
  }
  my $this_group = $groups[0]; # A File::KDBX::Group

  # Groups
  @groups = @{$this_group->groups}; # This group's groups
  # TODO - change!  In this loop, we add File::KeePass compatible keys.
  # This may become unsafe as File::KDBX makes some hashes readonly.
  my %knames = KeePass_KDBX_key_map(ref($state->{kdb}));
  foreach my $grp (@groups) { # Array of File::KDBX::Group objects
    foreach my $k (keys %knames) {
      $grp->{$k} = $grp->{$knames{$k}};
    }
    #warn "LHHD: path to $grp->{title}: ".Dumper(\@grps_to_root_names)."\n";
  }

  # Entries
  my @entries = @{$this_group->entries}; # This group's entries
  # In this loop, we add File::KeePass compatible keys, by way
  # of repulling each entry using get_entry_by_uuid().
  # This may become unsafe as File::KDBX makes some hashes readonly.
  foreach my $ent (@entries) { # Array of File::KDBX::Entry objects
    $ent = get_entry_by_uuid($state->{kdb}, $ent->uuid);
  }

  return (\@groups, \@entries);
}

# Helper function for cli_ls()
sub get_human_group_list($) {
  my $rGroup=shift @_;
  my $id_fmt = "%36s"; # KDBXv4
  $id_fmt = "%15d" if (ref($state->{kdb}) eq 'File::KeePass');
  my @list=();
  foreach my $grp (@{$rGroup}) {
    #push (@list, sprintf("$id_fmt %s/", getID($grp, 1), getLabel($grp)));
    my $title = getLabel($grp);
    #warn "LHHD: '$title' is_utf8:".int(utf8::is_utf8($title))."\n";
    push (@list, "$title/");
    #push (@list, &Dumper($grp)) if ($DEBUG > 2);
  }

  # If we're running in NO_UTF8 mode, we need to encode @list
  if ($NO_UTF8) {
    foreach my $grp_title (@list) {
      $grp_title = encode_if_utf8($grp_title, 1); # Encode out of UTF8
    }
  }

  return \@list;
}

# Helper function for cli_ls()
sub get_human_entry_list {
  my $rEntries=shift @_;
  my $start_num = shift @_ || 0;
  my @list=();
  my $i=0;
  my $d_len = length(scalar(@{$rEntries}) - 1 + $start_num);
  foreach my $ent (@{$rEntries}) {
    my $path = $state->{all_ent_paths_rev}->{getID($ent)};
    # As of kpcli v4.0, I chose to add "- NN" to duplicate entries
    # inside of a group. To make those navigable, I can't show the
    # title here, but instead must show the basename of the path.
    # See build_all_entry_paths() for where/how that's done.
    # If it were not for adding the "- NN", this code would and
    # otherwise should just use "my $title = getLabel($ent)" and not
    # have to fool with the utf-decoding of the $title here.
    my @path_pieces = reverse split("\0", $path);
    my $title_fp = shift @path_pieces; # Title from the path
    my $title = getLabel($ent);        # Title from the entry
    #warn "LHHD: '$title' is_utf8:".int(utf8::is_utf8($title))."\n";
    # $title_fp and $title can differ if there were duplicate entries
    # in a group and thusly "- NN" was added to those entries within
    # all_ent_paths_*. With the addition of UTF-8 support, we must
    # account for character encoding when comparing them...
    {
      local $NO_UTF8 = 0;  # Force these decodes() to operate
      if (decode_if_not_utf8($title_fp) ne decode_if_not_utf8($title)) {
        # The titles differed so use $title_fp and decode to UTF8 if needed
        my $is_title_utf8 = int(utf8::is_utf8($title));
        $title = $title_fp; # Cannot be UTF-8, came from all_ent_paths_rev
        $title = decode_if_not_utf8($title) if ($is_title_utf8);
      }
    }
    if (defined($ent->{'__in_old_dir'}) && $ent->{'__in_old_dir'}) {
      $title = "*OLD: " . $title;
    }

    # Grab the url and chop it down if needed
    my $url = getk($ent,'url');
    $url =~ s/^https?:\/\///i;
    $url =~ s/\/+$//;

    # Push this ent onto the list
    my $str = undef;
    my $str_format = "%".$d_len."d. %-40.40s %30.30s";
    if ($NO_UTF8) {
      # This is a really strange piece of code and it is needed because
      # sprintf() breaks on bytestrings that hold UTF8 characters. And
      # so, in NO_UTF8 mode, we decode, then sprintf, and then re-encode
      # these two strings. If we don't do that then sprintf(), just like
      # subtr(), deals with "bytes" and not "characters" and that breaks
      # our formatting/alignment under NO_UTF8.
      local $NO_UTF8 = 0;  # Force these de/encodes() to operate
      my $utf_t = decode_if_not_utf8($title); # Decode to UTF8
      my $utf_u = decode_if_not_utf8($url);   # Decode to UTF8
      $str = sprintf($str_format, $i + $start_num, $utf_t, $utf_u);
      $str = encode_if_utf8($str); # Encode out of UTF8
    } else {
      $str = sprintf($str_format, $i + $start_num, $title, $url);
    }
    push (@list, $str);
    $i++;
  }
  return \@list;
}

# Routine to hook into Term::ShellUI's exit on Ctrl-D functionality
sub eof_exit_hook {
  our $state;
  # We need a newline if cli_quit() will ask the user about saving
  if ($state->{kdb_has_changed}) { print "\n"; }
  # cli_quit() will handle user interaction and return a value for
  # the exit_hook of Term::ShellUI.
  $state->{in_eof_exit_hook} = 1;
  return cli_quit($state->{term},undef);
}

# Entry attachment handling
sub cli_attach {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint() || warn_if_file_changed()) {
    return;
  }

  my $target = $params->{args}->[0];
  my $ent=find_target_entry_by_number_or_path($target);
  if (! defined($ent)) {
    print no_entry_at_path_msg($target);
    return -1;
  }

  my $tmp_enth = entry_as_hash($ent);
  $state->{attach_changed} = 0;
  ATTACH_INTERFACE: while (1) {
    my @strings_keys = ();
    if (defined($tmp_enth->{binary}) && ref($tmp_enth->{binary}) eq 'HASH') {
      @strings_keys = sort keys %{$tmp_enth->{binary}};
    }
    my $strings_count = scalar(@strings_keys);
    my $t='';
    my $prompt = "Choose";
    if ($strings_count > 0) {
      $t .= show_helper_files_strings($tmp_enth,{f=>1,v=>1},'binary');
      $t .= "$prompt: (a)dd/(e)xport/(d)elete/(c)ancel/(F)inish? ";
    } else {
      $t .= "No files attached.\n";
      if (deny_if_readonly(0)) { print "$t\n"; return; }
      $t .= "$prompt: (a)dd/(c)ancel/(F)inish? ";
    }
    print "$t";
    COMMAND: while (my $key=get_single_key()) {
      if (lc($key) eq 'c' || ord($key) == 3) { # Cancel or ^C
        print "\n";
        delete $state->{attach_changed}; # Delete our temporary state var
        return;
      } elsif ($key =~ m/^[fF\r\n]$/) { # Finished (save)
        print "\n";
        if ($state->{attach_changed}) {
          # Recycle the entry if changes were made unless --no-recycle
          if (!(defined($opts->{'no-recycle'}) && int($opts->{'no-recycle'}))) {
            my $errmsg = recycle_entry($state, $ent);
            if (defined($errmsg)) { print "WARNING: $errmsg\n"; }
          }
          # Update the entry with the new binaries
          my $changes = { binary => $tmp_enth->{binary} };
          update_entry($state->{kdb}, $ent, $changes);
          delete $state->{attach_changed}; # Delete our temporary state var
          $state->{kdb_has_changed} = 1;
          RequestSaveOnDBChange();
        }
        return;
      } elsif (lc($key) eq 'd') {
        if (deny_if_readonly(2)) { return; }
        if (defined($tmp_enth->{binary}) && ref($tmp_enth->{binary}) eq 'HASH') {
          if ($strings_count < 2) {
            %{$tmp_enth->{binary}} = ();
            $state->{attach_changed}=1 if ($strings_count == 1);
          } else {
            print "\r". " "x60 ."\rWhich entry number do you want to delete? ";
            my $choice = get_single_line();
            if ($choice !~ m/^\d+$/ || $choice<1 || $choice > $strings_count) {
              print "\nInvalid number.";
            } else {
              delete($tmp_enth->{binary}->{$strings_keys[$choice-1]});
              $state->{attach_changed}=1;
            }
          }
          print "\n";
          next ATTACH_INTERFACE;
        }
      } elsif (lc($key) eq 'e') { # export
        my $to_export = undef;
        if (defined($tmp_enth->{binary}) && ref($tmp_enth->{binary}) eq 'HASH') {
          if ($strings_count < 1) {
            print "\n" .color('yellow'). 'Nothing it attached to export...' .
							color('clear')."\n";
          } elsif ($strings_count == 1) {
            $to_export = $strings_keys[0];
          } else {
            print "\r". " "x60 ."\rWhich entry number do you want to export? ";
            my $choice = get_single_line();
            if ($choice !~ m/^\d+$/ || $choice<1 || $choice > $strings_count) {
              print "\nInvalid number.";
            } else {
              $to_export = $strings_keys[$choice-1];
            }
          }
        }
        if (defined($to_export) && defined($tmp_enth->{binary}->{$to_export})) {
          my $homedir=get_user_homedir();
          my @path = File::Spec->splitdir($homedir);
          my $iv = File::Spec->catfile(@path, $to_export); # homedir/filename
          print "\n";
          my $filename = prompt_filename_from_user($self,"Path to file: ",$iv);
          if (! length($filename)) { next ATTACH_INTERFACE; }
          if (lc($OSNAME) !~ m/^mswin/) { $filename=expand_tildes($filename); }
          # If we're given a directory, assume the user wants to write into it
          if (-e -d $filename) { $filename .= '/' . $to_export; }
          if (-e -f $filename) {
            print color('yellow'). "WARNING: file already exists: $filename\n" .
                "Overwrite it? [y/N] " .color('clear');
            my $key=get_single_key();
            print "\n";
            if (lc($key) ne 'y') {
              next ATTACH_INTERFACE;
            }
          }
          my $fh = new FileHandle;
          if (! open($fh,'>', $filename)) {
            print "ERROR: cannot write to: $filename\n";
            next ATTACH_INTERFACE;
          }
          print $fh $tmp_enth->{binary}->{$to_export};
          close $fh;
          print "Saved to: $filename\n";
        }
        next ATTACH_INTERFACE;
      } elsif (lc($key) eq 'a') { # add
        if (deny_if_readonly(2)) { return; }
        if ($strings_count > 0 && $state->{kdb_ver} == 1) {
          print "\n" .color('yellow').
		'KeePass v1 files support only one attachment per entry.' .
							color('clear')."\n";
          next ATTACH_INTERFACE;
        }
        print "\n";
        my $filename = prompt_filename_from_user($self, "Path to file: ", "");
        if (! length($filename)) { next ATTACH_INTERFACE; }
        my $errmsg = do_attach_file($tmp_enth, $filename);
        if (defined($errmsg)) {
          print color('yellow'). "Error: $errmsg" .color('clear'). "\n";
        }
        next ATTACH_INTERFACE;
      } else {
        # Do nothing on invalid input
        next COMMAND;
      }
    }
  }

  #return $initial_value;
}
# Helper function for cli_attach
sub prompt_filename_from_user {
  my $self = shift @_;
  my $prompt = shift @_;
  my $initial_value = shift @_;

  my $term = get_prepped_readline_term();
  # Set a completion function for files
  my $old_compfunc=undef;
  if (my $attr = $term->Attribs) {
    # filename_completion_function works for Gnu Readline
    if (defined($attr->{filename_completion_function})) {
      $old_compfunc = $attr->{completion_entry_function};
      $attr->{completion_entry_function} =
			$attr->{filename_completion_function};
    }
  }
  # TODO - this need more testing with Perl readlines!!!
  if ($self->{term}->ReadLine eq 'Term::ReadLine::Perl') {
    #$readline::rl_completion_function = "rl_filename_list";
    $old_compfunc = $readline::rl_completion_function;
    $readline::rl_completion_function = \&my_nongnu_complete_files;
  } elsif ($self->{term}->ReadLine eq 'Term::ReadLine::Perl5') {
    $old_compfunc=$Term::ReadLine::Perl5::readline::rl_completion_function;
    $Term::ReadLine::Perl5::readline::rl_completion_function =
					\&my_nongnu_complete_files;
  }
  my $filename = $term->readline($prompt, $initial_value);
  $filename = decode_if_not_utf8($filename) if ($ALL_USER_INPUT_TO_UTF8);
  $filename =~ s/^\s+//; $filename =~ s/\s+$//; # Trim the input
  # Restore the old completion function
  if (defined($old_compfunc)) {
    if (my $attr = $term->Attribs) {
     $attr->{completion_entry_function} = $old_compfunc;
    }
    if ($self->{term}->ReadLine eq 'Term::ReadLine::Perl') {
      $readline::rl_completion_function = $old_compfunc;
    }
    if ($self->{term}->ReadLine eq 'Term::ReadLine::Perl5') {
      $Term::ReadLine::Perl5::readline::rl_completion_function =
							$old_compfunc;
    }
  }
  return $filename;
}
# Helper function for cli_attach
sub do_attach_file {
  my $entry = shift @_;
  my $path_to_file = shift @_;
  our $state;

  if (! -f $path_to_file) {
    return "File not found at: $path_to_file";
  }
  my $size = -s $path_to_file;
  if ($size > $MAX_ATTACH_SIZE) {
    my $sizeK = sprintf("%0.02f", $size / 1024);
    my $maxSizeK = sprintf("%0.02f", $MAX_ATTACH_SIZE / 1024);
    return "File is too large ($sizeK versus $maxSizeK KB maximum).";
  }
  my $fname_short = basename($path_to_file);
  if (defined($entry->{binary}->{$fname_short})) {
    return "An attachement named \"$fname_short\" already exists.\n";
  }
  # If we get this far we're OK to attach it
  open(my $fh,'<',$path_to_file) || return "Couldn't open file $path_to_file";
  binmode($fh, ":raw"); # Read raw binary (reported in SF patch #11).
  read($fh, my $buffer, $size);
  close $fh;
  if (length($buffer) != $size) {
    return "Couldn't read entire key file contents of $path_to_file.\n";
  }

  $entry->{binary}->{$fname_short} = $buffer;
  $state->{attach_changed}=1;
  return undef;
}
# Cross-platform attempt to find a user's homedir
sub get_user_homedir {
  if (lc($OSNAME) =~ m/^mswin/ &&
			defined($ENV{HOMEDRIVE}) && defined($ENV{HOMEPATH})) {
    #return $ENV{HOMEDRIVE} . $ENV{HOMEPATH}; # Windows
    return File::Spec->catpath($ENV{HOMEDRIVE}, $ENV{HOMEPATH}, undef);
  }
  my $home = $ENV{HOME} || $ENV{LOGDIR} || (getpwuid($<))[7] || undef; #Unix
  return $home;
}
# Expand tildes in filename
sub expand_tildes {
  my $filename = shift @_;
  # Page 253 of Perl Cookbook By Tom Christiansen, Nathan Torkington
  # "O'Reilly Media, Inc.", Aug 21, 2003
  $filename =~ s{ ^ ~ ( [^/]* ) }
		{ $1
			? (getpwnam($1))[7]
			: ($ENV{HOME} || $ENV{LOGDIR} || (getpwuid($<))[7])
		}ex;
  return $filename;
}

# Copied from Term::ShellUI and modified for enhanced Windows support
sub my_nongnu_complete_files {
    my ($str, $line, $start, $self) = @_;

    my ($volume,$directories,$file) = File::Spec->splitpath($str || '.', 0 );
    # This next line is for Windows tab completion on just "C:","D:", etc.
    if (length($volume) && !length($directories)) { $directories='/'; }
    my $dir = File::Spec->catpath($volume,$directories,'');

    # eradicate non-matches immediately (this is important if
    # completing in a directory with 3000+ files)
    $file = '' unless $str;
    my $flen = length($file);

    my @files = ();
    if(opendir(DIR, length($dir) ? $dir : '.')) {
        @files = readdir DIR;
        closedir DIR;
        # Only on Windows, we do this in a case insensitive way.
        if (lc($^O) =~ m/^mswin/) {
          # Case insensitive matching.
          @files = grep { lc(substr($_,0,$flen)) eq lc($file) } @files;
          # The case of the @files that we return must match what the
          # user has typed so far and that's what this substr does.
          @files = map { substr($_, 0, length($file), $file); $_; } @files;
        } else {
          @files = grep { substr($_,0,$flen) eq $file } @files;
        }
        # eradicate dotfiles unless user's file begins with a dot
        @files = grep { /^[^.]/ } @files unless $file =~ /^\./;
        # reformat filenames to be exactly as user typed
        @files = map { length($dir) ? ($dir eq '/' ? "/$_" : $dir.$_) : $_ } @files;
    } else {
        print("Couldn't read dir: $!\n");
    }

    # Tack trailing slashs on dirs
    my $dir_count = 0;
    foreach my $file_dir (@files) {
      if (-d $file_dir && $file_dir !~m/\/$/) { $file_dir .= '/'; $dir_count++; }
    }

    # If there are no subdirs in the list of completions and there is
    # only one file, then the completion is finished. Else, we need to
    # suppress_completion_append_character().
    if ($dir_count > 0 || scalar(@files) > 1) {
      __my_suppress_completion_append_character($self);
    }

    return @files;
}

sub cli_quit($$) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  my $in_eof_exit_hook = 0;
  if (defined($state->{in_eof_exit_hook})) {
    $in_eof_exit_hook = $state->{in_eof_exit_hook};
    $state->{in_eof_exit_hook} = 0; # Reset the state
  }

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  if ($state->{kdb_has_changed}) {
    print "WARNING: The database has changed and was not saved.\n" .
	"Really quit? [y/N] ";
    my $key=get_single_key(); print $key;
    if (lc($key) ne 'y') {
      print "\n";
      return -1; # It is not OK to quit
    }
  }

  if (defined($state->{placed_lock_file}) && -f $state->{placed_lock_file}) {
    unlink($state->{placed_lock_file});
  }
  delete($state->{placed_lock_file});
  $self->exit_requested(1);
  if ($in_eof_exit_hook) {
    print "\n"; # We need an prepended new-line when ^D was used to exit
  }
  PrintSupportMessage(1);
  return 0; # It's OK to quit
}

sub cli_autosave {
  my $self = shift @_;
  my $params = shift @_;
  my $no_print = shift @_ || 0;

  # This section of code handles "autosave -f"
  if (defined($params->{args})) {
    my %opts=();
    local @ARGV = @{$params->{args}};
    my $result = &GetOptions(\%opts, 'f');
    if ($opts{'f'}) {
      handle_autosaves();
      $no_print = 1;
    }
  }

  my $t="You can add entries to /$AUTOSAVES_DIR/ and, for each one, the save\n" .
	"command will write the open kdb to the filename in the url field\n" .
	"and with the entry's password. This can be used to keep copies\n" .
	"of your kdb files with alternative passwords that might only\n" .
	"be shared with the recipients during an emergency or at death.\n".
	"\n" .
	"The url field should only hold simple filenames (no paths) and\n" .
	"the files will be written to the same directory as the opened\n" .
	"Keepass file. There is no support for keyfile, only passwords.\n" .
	"\n" .
	"When /$AUTOSAVES_DIR/ entries exist, the save command shows\n" .
	"them and prompts the user for confirmation before execution.\n" .
	"\n" .
	"To process autosaves manually, apart from the save command,\n" .
	"issue the command: autosave -f\n" .
	"";
  if ($no_print) { return $t; } else { print $t; }
}

sub cli_versions($$) {
  my $self = shift @_;
  my $params = shift @_;
  my %opts=();
  {
    local @ARGV = @{$params->{args}};
    my $result = &GetOptions(\%opts, 'v');
  }
  if ($opts{'v'}) {
    return cli_version(shift, { args => ['-vv'] });
  } else {
    return cli_version(shift, { args => ['-v'] });
  }
}
sub cli_version($$) {
  my $self = shift @_;
  my $params = shift @_;
  our $state;

  if (recent_sigint()) { return undef; } # Bail on SIGINT

  # Users can provide a -f option to show the password. We use GetOptions
  # to parse this command line, and $target holds that target.
  my $target='';
  my %opts=();
  {
    local @ARGV = @{$params->{args}};
    my $result = &GetOptions(\%opts, 'v', 'vv');
  }

  # Without a -v or -vv, simply print the kpcli version
  if (! ($opts{'v'} || $opts{'vv'})) {
    print "$VERSION\n";
    return;
  }

  # Items for -v
  my @modules_reported_on = (); # So we don't double-report in -vv
  if ($opts{'v'} || $opts{'vv'}) {
    print "kpcli: $VERSION\n";
    # Perl version
    my $pv = $PERL_VERSION;
    if (! length($pv)) {
      $pv = $]; # For perl versions prior to 5.6.0
    }
    print "Perl: $pv\n";
    # Operating System
    my $OS=$OSNAME;
    if (lc($OSNAME) eq 'linux') {
      my $lsbr = load_lsb_release();
      if (defined($lsbr) && defined($lsbr->{'DISTRIB_DESCRIPTION'})) {
        $OS .= " (" . $lsbr->{'DISTRIB_DESCRIPTION'} . ")";
      }
    } elsif (lc($OSNAME) eq 'darwin') {
      my $osver = get_macos_version();
      if (defined($osver) && defined($osver->{'ProductName'}) && 
					defined($osver->{'ProductVersion'})) {
        my $prodname = $osver->{'ProductName'};
        if ($osver->{'ProductName'} =~ m/mac os x|macos/i) {
          $prodname = 'macOS'; # More modern nomenclature
        }
        $OS .= " ($prodname ".$osver->{'ProductVersion'}.")";
      }
    } elsif (lc($OSNAME) eq 'mswin') {
      if (! is_loaded('Win32')) {
        runtime_load_module(\%OPTIONAL_PM,'Win32',undef);
      }
      if (is_loaded('Win32')) {
        $OS .= " (" . Win32::GetOSDisplayName() . ")";
      }
    }
    print "Operating system: $OS\n";
    print "ReadLine being used: " . $term->{term}->ReadLine . "\n";
    print "\n";

    print "Pivotal Perl Modules for kpcli\n";
    my @modules = qw(File::KeePass File::KDBX Term::ShellUI Term::ReadKey Term::ReadLine);
    my @missing_modules = ();
    foreach my $module (sort keys %OPTIONAL_PM) {
      if (is_loaded($module)) {
        push @modules, $module;
      } else {
        push @missing_modules, $module;
      }
    }
    # There are a few OS-specific modules that we'd also
    # like to report on. These are down-stream dependencies
    # of %OPTIONAL_PM modules.
    my %OSspecificModules = (
	darwin  => [ qw( Mac::Pasteboard )  ],
	mswin32 => [ qw( Win32::Clipboard ) ],
	);
    my $osname = lc($OSNAME);
    if (defined($OSspecificModules{$osname})) {
      foreach my $module (@{$OSspecificModules{$osname}}) {
        if (is_loaded($module)) {
          push @modules, $module;
        } else {
          push @missing_modules, $module;
        }
      }
    }
    foreach my $module (@modules) {
      no strict 'refs';
      my $vstr=$module . "::VERSION";
      if (defined(${$vstr})) {
        print " * $module: " . ${$vstr} . "\n";
      } elsif (is_loaded($module)) {
        print " * $module: ** unknown version **\n";
      } else {
        print " * $module: not installed (recommended)\n";
      }
    }
    foreach my $module (@missing_modules) {
      print " * $module: not installed (optional)\n";
    }

    @modules_reported_on = (@modules, @missing_modules);
  }

  # Additional items for -vv
  if ($opts{'vv'}) {
    my @loaded_modules = grep(/\.pm$/, nsort(keys %INC));
    my $sep = File::Spec->catfile('', '');
    my @mod_names = ();
    foreach my $mod_path (@loaded_modules) {
      my $mod_name = $mod_path;
      $mod_name =~ s/\.pm$//;
      $mod_name =~ s%[\/]%::%g;
      # Skip modules that we've already reported on
      if (scalar(grep(/^\Q$mod_name\E$/, @modules_reported_on))) { next; }
      push @mod_names, $mod_name;
    }
    print "\nAll Other Loaded Perl Modules\n";
    foreach my $module (@mod_names) {
      no strict 'refs';
      my $vstr=$module . "::VERSION";
      my $modver = ${$vstr} || 'unknown';
      print " * $module: $modver\n";
    }
  }
}

# Used info from https://gist.github.com/natefoo/814c5bf936922dad97ff
# to enhance this for situations where /etc/lsb-release is missing.
# This sub works hard to populate DISTRIB_DESCRIPTION, but nothing else.
sub load_lsb_release {
  my $fh = new FileHandle;
  # The first of these files that works is what we use.
  my @release_files = qw(/etc/lsb-release /etc/os-release /usr/lib/os-release);
  foreach my $file (@release_files) {
    if (-f $file && open($fh,'<', $file)) {
      my @lines = <$fh>;
      close $fh;
      my %d = ();
      foreach my $l (@lines) {
        chomp $l;
        my ($k,$v) = split(/=/, $l, 2);
        $d{$k} = $v;
      }
      # This copies PRETTY_NAME from /.../os-release into key
      # DISTRIB_DESCRIPTION which would have been in /etc/lsb-release.
      if (!defined($d{DISTRIB_DESCRIPTION}) && defined($d{PRETTY_NAME})) {
        $d{DISTRIB_DESCRIPTION} = $d{PRETTY_NAME};
      }
      $d{data_from} = $file;
      return \%d;
    }
  }
  # If we got this far, we failed to get data from an /etc/ file, and
  # so now we'll try running lsb_release -a.
  my $lsbr_a = lsb_release_a();
  if (defined($lsbr_a) && defined($lsbr_a->{'Description'})) {
    $lsbr_a->{DISTRIB_DESCRIPTION} = $lsbr_a->{Description};
    return $lsbr_a;
  }
  # These may not have /etc/foo-release files or lsb_release.
  my @version_files = qw(/etc/antix-version /etc/slackware-version);
  foreach my $file (@version_files) {
    if (-f $file && open($fh,'<', $file)) {
      my @lines = <$fh>;
      close $fh;
      if (scalar(@lines)) {
        my %d;
        chomp $lines[0];
        $d{DISTRIB_DESCRIPTION} = $lines[0];
        $d{data_from} = $file;
        return \%d;
      }
    }
  }

  return undef;
}
# Tries to pull Linux OS details from "lsb_release -a"
sub lsb_release_a {
  my @paths = split/:/, $ENV{PATH};
  EXE_PATH: foreach my $dir (@paths) {
    my $lsb_release = $dir.'/lsb_release';
    if (-e -x $lsb_release) {
      my @lines = `"$lsb_release" -a 2>/dev/null`;
      my %d = ();
      foreach my $l (@lines) {
        chomp $l;
        my ($k,$v) = split(/:\s*/, $l, 2);
        $d{$k} = $v;
      }
      $d{data_from} = "$lsb_release -a";
      return \%d;
    }
  }
  return undef;
}

sub get_macos_version {
  my $fh = new FileHandle;
  my $fSystemVersion = '/System/Library/CoreServices/SystemVersion.plist';
  if (-f $fSystemVersion && open($fh,'<',$fSystemVersion)) {
    my @lines = <$fh>;
    close $fh;
    my %d = ();
    my ($k,$v) = (undef,undef);
    foreach my $l (@lines) {
      chomp $l;
      next if ($l !~ m/\s*<(key|string)>/);
      if ($l =~ m/\s*<key>([^<]+)</) { $k = $1; }
      if ($l =~ m/\s*<string>([^<]+)</) { $v = $1; }
      if (defined($k) && defined($v)) {
        $d{$k} = $v;
        ($k,$v) = (undef,undef);
      }
    }
    return \%d;
  }
  return undef;
}

# Function to nag the user about saving each time the DB is modified
sub RequestSaveOnDBChange {
  our $state;

  # If the db hasn't changed don't bother the user
  if (! $state->{kdb_has_changed}) {
    return -1;
  }

  # If this is a newly created file we don't bother the user with
  # asking to save after every change.
  if (! (defined($state->{kdb_file}) && length($state->{kdb_file}))) {
    return -1;
  }

  print "Database was modified. Do you want to save it now? [y/N]: ";
  my $key=get_single_key(); print "$key\n";
  if (lc($key) ne 'y') {
    return;
  }

  # Calling cli_save() should be silent and safe at this point.
  return cli_save(undef);
}

sub GetMasterPasswd {
  my $prompt = shift @_ || "Provide the master password: ";
  return GetPassword($prompt,$PASSWD_ECHO_CHAR);
}

sub GetMasterPasswdDoubleEntryVerify {
  my $prompt = shift @_ || undef;
  my $master_pass=GetMasterPasswd($prompt);
  if (recent_sigint()) { return undef; } # Bail on SIGINT

  if (length($master_pass) == 0) { return ''; }

  $prompt = "Retype to verify: ";
  my $checkval = GetPassword($prompt,$PASSWD_ECHO_CHAR);
  chomp $checkval;
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  if ($master_pass ne $checkval) {
    print "Passwords did not match...\n";
    return undef;
  }

  return $master_pass;
}

sub GetPassword {
  my $prompt = shift @_;
  my $echo_char = shift @_ || '';

  if (length($echo_char) > 1) {
    warn "GetPassword() cannot accept an \$echo_char of more than one char.\n";
    $echo_char='';
  }

  $|=1; # Needed to flush STDOUT on Windows cmd prior to calling ReadMode
  ReadMode('noecho');
  ReadMode('raw');
  my $master_pass = '';
  print $prompt;
  CHAR: while (1) {
    my $c;
    do {
      Time::HiRes::sleep(0.05);
    } until defined($c = ReadKey(-1));
    last if $c =~ m/[\n\r]/;
    if (ord($c) == 3) { # ^C
      print "\n";
      ReadMode('normal');
      kill SIGINT, $$; # Due to raw mode, I must send the SIGINT to myself.
      return '';
    } elsif (ord($c) == 127 || ord($c) == 8) { # backspace (Linux/Windows)
      if (length($master_pass) && length($echo_char)) {
        print chr(8)." ".chr(8);
        chop($master_pass);
      }
      next CHAR;
    } elsif (ord($c) == 21) { # ^U
      my $passlen=length($master_pass);
      print chr(8)x$passlen." "x$passlen.chr(8)x$passlen;
      $master_pass = '';
      next CHAR;
    }
    if (length($echo_char)) { print $echo_char; }
    #print "*".ord($c);
    $master_pass .= $c;
  }
  ReadMode('normal');
  chomp $master_pass;
  my $min_display_length = 25;
  if (length($master_pass) < $min_display_length) {
    print "$echo_char"x($min_display_length - length($master_pass));
  }
  print "\n"; $|=1;
  if (recent_sigint()) { return undef; } # Bail on SIGINT
  return $master_pass;
}

sub MyGetOpts {
  my %opts=();
  my @params = (
	"kdb=s", "key=s", "pwfile=s", "histfile=s", "help", "h",
	"noutf8", "readonly", "no-recycle", "timeout=i", "command=s@",
	"nopwstars", "nopwprint", "pwsplchars=s", "xpxsecs=i", "xclipsel=s",
	"pwwords=s", "pwlen=i", "pwscmin=i", "pwscmax=i", "kpxcexe=s");
  my $result = &GetOptions(\%opts, @params);

  my $use_help_msg = "Use --help to see information on command line options.";

  # Set any undefined booleans to 0
  foreach my $param (@params) {
    if ($param !~ m/=/ && (! defined($opts{$param}))) {
      $opts{$param} = 0; # Booleans
    }
  }

  # If the user asked for help give it and exit
  if ($opts{help} || $opts{h}) {
    print GetUsageMessage();
    exit;
  }

  # If GetOptions failed it told the user why, so let's exit.
  if (! int($result)) {
    print "\n" . $use_help_msg . "\n";
    exit;
  }

  # Allow the user to override the history file
  if (defined($opts{histfile}) && length($opts{histfile})) {
    our $HISTORY_FILE = $opts{histfile};
  } else {
    if (lc($OSNAME) =~ m/^mswin/) {
      our $HISTORY_FILE = $ENV{USERPROFILE} . "/.$APP_NAME-history";
    } else {
      our $HISTORY_FILE = "~/.$APP_NAME-history";
    }
  }

  # If the user asked for --nopwstars, clear the $PASSWD_ECHO_CHAR
  if ($opts{nopwstars}) {
    our $PASSWD_ECHO_CHAR = '';
  }

  # Sanity check the use of --pwsplchars
  my @sc_warns = ();
  if (defined($opts{'pwsplchars'})) {
    if (!(length($opts{'pwsplchars'}))) {
      push @sc_warns, "You removed all special characters."
    }
    my $sc_minus_underscore = $opts{'pwsplchars'};
    $sc_minus_underscore =~ s/_//g;
    if ($sc_minus_underscore =~ m/\w/) {
      push @sc_warns, "Contains normal word characters.";
    }
    if ($opts{'pwsplchars'} =~ m/[^[:print:]]/) {
      push @sc_warns, "Contains non-printable characters.";
    }
    my @sc = split(//, $opts{'pwsplchars'});
    if (scalar(@sc) != scalar(uniq(@sc))) {
      push @sc_warns, "One or more characters are duplicated.";
    }
    if (scalar(@sc_warns)) {
      print color('bold yellow') .
	"WARNING(s) regarding --pwsplchars for password generation:\n" .
	color('clear') . color('yellow') .
		' * ' . join("\n * ", @sc_warns) . "\n" .
	color('clear');
    }
  } else {
    $opts{'pwsplchars'} = '_'; # The default list is just underscore
  }
  my @special_chars = split(//, $opts{'pwsplchars'});
  $opts{'pwsplchars'} = \@special_chars;

  my @errs=(); # Collects any errors that we find

  # Start by looking to see if the user gave just one bare argument and,
  # if so, assume that it is a file and place it into --kdb.
  my @args_left = @ARGV;
  if (scalar(@args_left) > 1) {
    push @errs, "only one bare argument (a filename) is allowed.";
  } elsif (scalar(@args_left) > 0) {
    if (defined($opts{kdb}) && length($opts{kdb})) {
      push @errs, "both --kdb and a bare argument filename is not allowed.";
    } else {
      $opts{kdb} = shift @args_left; # Place it where --kdb would have been
    }
  }

  if (defined($opts{kdb}) && length($opts{kdb}) && (! -e $opts{kdb})) {
    push @errs, "for option --kdb=<file.kdb>, the file must exist.";
  }

  if ( defined($opts{pwfile}) && (! -f -r $opts{pwfile}) ) {
    push @errs, "for option --pwfile=<file>, the file must exist.";
  }

  if (defined($opts{key}) && length($opts{key}) && (! -e $opts{key})) {
    push @errs, "for option --key=<file.key>, the file must exist.";
  }

  if (defined($opts{xpxsecs}) && length($opts{xpxsecs})) {
    if (! ($opts{xpxsecs} =~ m/^\d+$/)
		|| $opts{xpxsecs} < 1 || $opts{xpxsecs} > 60 ) {
      push @errs, "--xpxsecs must be between 1 and 60.";
    }
  } else {
    $opts{xpxsecs} = 10; # Default is 10 seconds
  }

  if (defined($opts{pwwords}) && length($opts{pwwords}) &&
						(! -e $opts{pwwords})) {
    push @errs, "for option --pwwords=<file>, the file must exist.";
  }

  if (defined($opts{pwlen})) {
    if ($opts{pwlen} < 1) {
      push @errs, "--pwlen of less than 1 is nonsensical.";
    }
    our ($DEFAULT_PASSWD_LEN, $DEFAULT_PASSWD_MAX);
    $DEFAULT_PASSWD_LEN = $opts{pwlen};
    if ($DEFAULT_PASSWD_LEN > $DEFAULT_PASSWD_MAX) {
      $DEFAULT_PASSWD_MAX = $DEFAULT_PASSWD_LEN;
    }
  }

  # Set defaults for --pwscmin=i and --pwscmax=i
  if (! defined($opts{pwscmin})) { $opts{pwscmin} = 1; }
  if (! defined($opts{pwscmax})) { $opts{pwscmax} = 9999; }
  if ($opts{pwscmax} < $opts{pwscmin}) {
    push @errs, "--pwscmax cannot exceed --pwscmin, which defaults to 1.";
  }

  # Sanity check the --xclipsel option if provided
  if (defined($opts{xclipsel}) && length($opts{xclipsel})) {
    # First determine if --xclipsel is relevant and exit if not
    if (! is_loaded("Clipboard")) {
      print "--xclipsel is only relevant if the Clipboard module is installed.\n";
      exit;
    } elsif ($opts{xclipsel} eq 'help' && $Clipboard::driver ne 'Clipboard::Xclip') {
      print "--xclipsel is only relevant on systems with X11.\n";
      exit;
    }
    # Now validate the --xclipsel choice
    if (is_loaded("Clipboard") && $Clipboard::driver eq 'Clipboard::Xclip') {
      my @x11_sels = $Clipboard::driver->all_selections();
      unshift @x11_sels, 'all';
      if (! scalar(grep(/^$opts{xclipsel}$/, @x11_sels))) {
        my $default = $Clipboard::driver->favorite_selection();
        # Indicate the default by wrapping it in brackets
        SEL: foreach my $i (0..$#x11_sels) {
          if ($x11_sels[$i] eq $default) {
            $x11_sels[$i] = '['.$default.']';
            last SEL;
          }
        }
        my $usemsg = "--xclipsel must be one of: ".join(", ", @x11_sels);
        if ($opts{xclipsel} eq 'help') {
          print $usemsg . "\n"; exit;
        } else {
          push @errs, $usemsg;
        }
      }
    }
  }

  if (defined($opts{kpxcexe})) {
     if (! (-f -x $opts{kpxcexe} && can_kpxc($opts{kpxcexe}, $KPXC_MIN_VER))) {
       print "--kpxcexe does not point to a KeePassXC binary >= v$KPXC_MIN_VER.\n";
       exit -1;
     }
  }

  if (scalar(@errs)) {
    warn "There were errors:\n" .
	"  " . join("\n  ", @errs) . "\n\n";
    print $use_help_msg . "\n";
    exit;
  }

  return \%opts;
}

sub PrintSupportMessage {
  my $frequency = shift @_ || 20; # Every twentieth command by default

  my $t = color('yellow') .
	"Please consider supporting kpcli development by sponsoring its " . 
	"author:\nhttps://github.com/sponsors/hightowe" . color('clear');

  # We need to keep count of how often we're called (command count)
  our $state;
  if (! defined($state->{support_msg_cmd_count})) {
    $state->{support_msg_cmd_count} = 0;
  }
  $state->{support_msg_cmd_count}++;

  # Show the message every Nth command run, based on $frequency
  if ( ($state->{support_msg_cmd_count} % $frequency) == 0) {
    print $t . "\n";
  }
  # Note that we are intentionally *not* returning anything here!!!
}

sub GetUsageMessage {
  my $parmlen = 14;
  my $col1len = $parmlen + 3;
  my $pwlen = our $DEFAULT_PASSWD_LEN;
  my @params = (
    [ 'kdb=s'      => 'Optional KeePass database file to open (must exist).' ],
    [ 'key=s'      => 'Optional KeePass key file (must exist).' ],
    [ 'pwfile=s'   => 'Read master password from file instead of console.' ],
    [ 'histfile=s' => 'Specify your history file (or perhaps /dev/null).' ],
    [ readonly     => 'Run in read-only mode; no changes will be allowed.' ],
    [ "timeout=i"  => 'Lock interface after i seconds of inactivity.' ],
    [ 'command=s'  => "Run a command and exit (no interactive session).\n" .
                      ' 'x$col1len .
                      "Multiple --command parameters can be used." ],
    [ 'no-recycle' =>
		'Don\'t store entry changes in /Backup or "/Recycle Bin".' ],
    [ 'pwwords=s'  => "File of words for building word-based passwords." ],
    [ 'pwsplchars=s' => 'The special characters used in password generation.' ],
    [ 'pwlen=i'    => "Length of generated passwords (default is $pwlen)." ],
    [ 'pwscmin=i'  => "Min number of special chars in generated passwords." ],
    [ 'pwscmax=i'  => "Max number of special chars in generated passwords." ],
    [ 'nopwstars'  => "Don't show star characters (*) for password input." ],
    [ 'nopwprint'  => "Don't print the pw red on red in the show command." ],
    [ 'noutf8'     => "Disable all UTF-8 support, first added in v4.1." ],
    [ 'xpxsecs=i'  =>
		'Seconds to wait until clearing the clipboard for xpx.' ],
    [ 'xclipsel=s' => 'X11 clipboard to use; "--xclipsel help" for choices.' ],
    [ 'kpxcexe=s'  => 'Path to a KeePassXC binary, used to import KDBX4 files.' ],
    [ help         => 'This message.' ],
  );
  my $t="Usage: $APP_NAME [--kdb=<file.kdb>] [--key=<file.key>]\n" .
  "\n";
  foreach my $param (@params) {
    my $fmt = '  %-'.$parmlen.'s %s';
    $t .= sprintf("$fmt\n", '--'.$param->[0], $param->[1]);
  }
  $t .= "\n" .
  "Run kpcli with no options and type 'help' at its command prompt to learn\n" .
  "about kpcli's commands.\n" .
  "";
  return $t;
}

# Because Term::ShellUI has a fixed width (%20s) for the command length
# and we don't need nearly that much, we had to implement our own help
# function instead of using the built-in help_call() method.
sub my_help_call($) {
  my $term = shift @_;
  # @_ now holds: [Term::ShellUI->{commands}, <optional: specific command>]
  # If the user is asking for detailed help on a specific command, do that
  if (scalar(@_) > 1) {
    $term->help_call(undef, @_);
    return;
  }
  # If no specific command was requested, show the command summaries
  my $help = $term->get_all_cmd_summaries($term->commands());
  $help =~ s/^ {12}//gm; # Trim some leading spaces off of each line of output
  print $help;
  print "\n" .
	"Type \"help <command>\" for more detailed help on a command.\n";
  return 0;
}

########################################################################
# Command Completion Routines ##########################################
########################################################################
sub complete_groups {
  my $self = shift;
  my $cmpl = shift;
  our $state;

  # The string that Term::ShellUI is trying to complete is $compl_str.
  # For paths that have spaces in them, this string will be only the
  # last word, or an empty string if the cursor is sitting on whitespace,
  # such as "\ <tab>" ....
  my $compl_str = $cmpl->{str};
  # Place the string (token) that the user is trying to complete into $path.
  my $path = $cmpl->{tokens}->[$cmpl->{tokno}];
  # If the cursor isn't at the end of the sting, chop $path to that length.
  if (length($path) > $cmpl->{tokoff}) {
    $path = substr($path, 0, $cmpl->{tokoff});
  }

  my $orig_path = $path; # Before we make it absolute
  my $is_path_abs = 0;
  $is_path_abs = 1 if ($path =~ m%^/%);
  my $pwd = get_pwd();
  if (! $is_path_abs) {
    $path="$pwd/$path";
  }

  my $srch_path=normalize_path_string($path);

  my @poss_grps = ();
  if ($path =~ m/\/$/ && defined($state->{all_grp_paths_fwd}->{$srch_path})) {
    # If our search end with a "/" and is a valid group
    @poss_grps = grep(/^\Q$srch_path\E\0[^\0]+\0?$/, sort keys %{$state->{all_grp_paths_fwd}});
  } else {
    @poss_grps = grep(/^\Q$srch_path\E[^\0]*\0?$/, sort keys %{$state->{all_grp_paths_fwd}});
  }

  my @completions=();
  foreach my $comp (sort @poss_grps) {
    # The full path that is being tabbed against
    my $norm_path = normalize_path_string($path);
    # Isolate the characters *past* the $norm_path
    my $next_chars = substr($comp, length($norm_path));
    # Kill leading \0 if it exists, else humanize_path() adds an extra /
    $next_chars =~ s/^\0//;
    # Append our humanized options to the end of the user's $compl_str, and
    # be sure we don't get a UTF-8 encoded string back.
    my $comp_path = $compl_str . humanize_path($next_chars, 0);
    # These are groups, so we always want to add a tailing /
    $comp_path .= '/' if ($comp_path !~ m%/$%);
    #print "\nLHHD: comp / norm_path / next / comp_path:\n".Dumper($comp,$norm_path, $next_chars, $comp_path)."\n";
    push @completions, $comp_path;
  }

#  print Dumper(\@poss_grps, \@completions)."\n";
#  print "\ncomplete_groups: ".Dumper($srch_path, \@poss_grps, \@completions)."\n";
#  print Dumper("\ngrp:",\@completions)."\n";
#  $self->completemsg(" *\"$compl_str\"*\"$orig_path\"*\"$path\" is_path_abs=$is_path_abs\n");

  # If we are about to return only one completion result, we need to first
  # test to see if any other subdirs are below it and, if so, suppress the
  # completion append character so that the user can keep tab completing
  # into lower level directories.
  if (scalar(@completions) == 1) {
    my @all_subdirs = grep(/^\Q$srch_path\E[^\0]*(\0[^\0]+)?/,
                                sort keys %{$state->{all_grp_paths_fwd}});
    if (scalar(@all_subdirs) > 0) {
      __my_suppress_completion_append_character($self);
    }
  }

  return \@completions;
}

sub complete_entries {
  my $self = shift;
  my $cmpl = shift;
  our $state;

  #print "LHHD:\n".Dumper($cmpl)."\n";

  # The string that Term::ShellUI is trying to complete is $compl_str.
  # For paths that have spaces in them, this string will be only the
  # last word, or an empty string if the cursor is sitting on whitespace,
  # such as "\ <tab>" ....
  my $compl_str = $cmpl->{str};
  # Place the string (token) that the user is trying to complete into $path.
  my $path = $cmpl->{tokens}->[$cmpl->{tokno}];
  # If the cursor isn't at the end of the sting, chop $path to that length.
  if (length($path) > $cmpl->{tokoff}) {
    $path = substr($path, 0, $cmpl->{tokoff});
  }

  my $orig_path = $path; # Before we make it absolute
  my $is_path_abs = 0;
  $is_path_abs = 1 if ($path =~ m%^/%);
  if (! $is_path_abs) {
    $path=get_pwd() . "/" . $path;
  }

  my $srch_path=normalize_path_string($path);

  my @completions=();

  my @poss_grps = undef;
  # Tabbed on a specific group
  if (defined($state->{all_grp_paths_fwd}->{$srch_path}) && $compl_str =~ m%/$%) {
    @poss_grps = grep(/^\Q$srch_path\E\0[^\0]+$/, sort keys %{$state->{all_ent_paths_fwd}});
  } else {
    @poss_grps = grep(/^\Q$srch_path\E[^\0]+$/, sort keys %{$state->{all_ent_paths_fwd}});
  }
  # Tabbed on a specific entry (these are excluded above)
  if (defined($state->{all_ent_paths_fwd}->{$srch_path})) {
    push @poss_grps, $srch_path;
  }

  foreach my $comp (sort @poss_grps) {
    # The full path that is being tabbed against
    my $norm_path = normalize_path_string($path);
    # Isolate the characters *past* the $norm_path
    my $next_chars = substr($comp, length($norm_path));
    # Kill leading \0 if it exists, else humanize_path() adds an extra /
    $next_chars =~ s/^\0//;
    # Append our humanized options to the end of the user's $compl_str, and
    # be sure we don't get a UTF-8 encoded string back.
    my $comp_path = $compl_str . humanize_path($next_chars, 0);
    # print "\nLHHD: comp / norm_path / next / comp:\n".Dumper($comp,$norm_path, $next_chars, $comp_path)."\n";
    push @completions, $comp_path;
  }

#  print "\ncomplete_entries: ".Dumper($srch_path, \@poss_grps, \@completions)."\n";
#  print Dumper("ent:",\@completions)."\n";
#  $self->completemsg(" *\"$compl_str\"*\"$orig_path\"*\"$path\" is_path_abs=$is_path_abs\n");

  return \@completions;
}

sub complete_groups_and_entries {
  my $self = shift;
  my $cmpl = shift;

  my $groups = complete_groups($self,$cmpl);
  my $entries = complete_entries($self,$cmpl);

  # Merge and sort the groups and entries
  my @completions = sort (@{$groups}, @{$entries});

  return \@completions;
}

# In Term::ReadLine::Gnu, suppress_completion_append_character() works,
# but in Term::ReadLine::Perl and Term::ReadLine::Perl5 it does not, and
# so we get to the outcome via $readline::rl_completer_terminator_character.
sub __my_suppress_completion_append_character($) {
  my $self = shift;
  if (defined($self) && $self->{term}->ReadLine eq 'Term::ReadLine::Gnu') {
    $self->suppress_completion_append_character();
  } else {
    # For Term::ReadLine::Perl
    # From Term/ReadLine/readline.pm
    #  - package readline;
    if (defined($readline::rl_completer_terminator_character)) {
      $readline::rl_completer_terminator_character='';
    }
    # For Term::ReadLine::Perl5
    # From Term/ReadLine/Perl5/readline.pm
    #  - package Term::ReadLine::Perl5::readline;"
    if (defined(
	$Term::ReadLine::Perl5::readline::rl_completer_terminator_character)) {
      $Term::ReadLine::Perl5::readline::rl_completer_terminator_character='';
    }
  }
}

########################################################################
# Rijndael encrypt/decrypt routines - borrowed from File::KeePass ######
########################################################################
sub decrypt_rijndael_cbc {
    my ($buffer, $key, $enc_iv) = @_;
    my $cipher = Crypt::Rijndael->new($key, Crypt::Rijndael::MODE_CBC());
    $cipher->set_iv($enc_iv);
    $buffer = $cipher->decrypt($buffer);
    my $extra = ord(substr $buffer, -1, 1);
    substr($buffer, length($buffer) - $extra, $extra, '');
    return $buffer;
}
sub encrypt_rijndael_cbc {
    my ($buffer, $key, $enc_iv) = @_;
    my $cipher = Crypt::Rijndael->new($key, Crypt::Rijndael::MODE_CBC());
    $cipher->set_iv($enc_iv);
    my $extra = (16 - length($buffer) % 16) || 16; # pad so we can trim
    $buffer .= chr($extra) for 1 .. $extra;
    return $cipher->encrypt($buffer);
}
sub composite_master_pass($$$) {
  my ($style, $pass, $key_file) = @_;
  if ($style eq 'File::KeePass') {
    return composite_master_pass_FileKeePass($pass, $key_file);
  } elsif ($style eq 'File::KDBX') {
    return composite_master_pass_FileKDBX($pass, $key_file);
  }
  die "Cannot composite_master_pass() for style = $style\n";
}
sub composite_master_pass_FileKeePass($$) {
  my ($pass, $key_file) = @_;
  # composite password in case of key file
  if (defined $key_file and length($key_file) and -f $key_file) {
    # KeePass v2.03 and higher has native key file support, and so we
    # use that if we have it.
    if (version->parse($File::KeePass::VERSION) >= version->parse('2.03')) {
      return [$pass, $key_file];
    }
    # TODO - at some point, when File::KeePass v2.03 is very mainstream,
    # the code to the end of this if block should be removed. It allowed
    # support for key files for *.kdb files before File::KeePass supported
    # that natively. File::KeePass now also supports that for *.kdbx.
    open(my $fh,'<',$key_file) || die "Couldn't open key file $key_file: $!\n";
    my $size = -s $key_file;
    read($fh, my $buffer, $size);
    close $fh;
    if (length($buffer) != $size) {
      die "Couldn't read entire key file contents of $key_file.\n";
    }

    $pass = substr(sha256($pass),0,32);
    if ($size == 32) {
      $pass .= $buffer;
    } elsif ($size == 64) {
      for (my $i = 0; $i < 64; $i += 2) {
        $pass .= chr(hex(substr($buffer,$i,2)));
      }
    } else {
      $pass .= substr(sha256($buffer),0,32);
    }
    # TODO - this marks the "end of the block" noted above.
  }

  return $pass;
}
sub composite_master_pass_FileKDBX($$) {
  my ($pass, $key_file) = @_;
  my @components = ();
  if (defined $pass and length($pass)) {
    push @components, File::KDBX::Key->new({ password => $pass });
  }
  if (defined $key_file and length($key_file) and -f $key_file) {
    push @components, File::KDBX::Key->new({ file => $key_file });
  }
  return File::KDBX::Key->new({ composite => \@components });
}
sub put_master_passwd($) {
  my $master_pass = shift @_;
  our $state;
  $state->{'master_pass_key'}='';
  $state->{'master_pass_key'} .= chr(int(255 * rand())) for 1..16;
  $state->{'master_pass_enc_iv'}='';
  $state->{'master_pass_enc_iv'} .= chr(int(255 * rand())) for 1..16;
  $master_pass='CLEAR:' . $master_pass;
  $state->{'master_pass'}=encrypt_rijndael_cbc($master_pass,
		$state->{'master_pass_key'}, $state->{'master_pass_enc_iv'});
  return 0;
}
sub get_master_passwd() {
  our $state;
  my $master_pass=decrypt_rijndael_cbc($state->{master_pass},
		$state->{'master_pass_key'}, $state->{'master_pass_enc_iv'});
  if ($master_pass=~s/^CLEAR://) {
    return $master_pass;
  } else {
    die "Failed to properly decrypt my copy of the master password.\n";
  }
}

# This routine checks to see if the file has changed on disk and warns if so
sub warn_if_file_changed {
  our $state;

  my $file = $state->{kdb_file} || '';
  if (! length($file)) { return 0; } # If no file was opened, don't warn
  my $file_md5 = Digest::file::digest_file_hex($file, "MD5");
  if ($state->{kdb_file_md5} ne $file_md5) {
    print color('bold yellow') . "WARNING:" . color('clear') .
        color('red') .
               " The file has changed on disk since kpcli opened it!\n" .
        "         It may be opened elsewhere. Continue anyway? [y/N] " .
        color('clear');
    my $key=get_single_key(); print "$key\n";
    if (lc($key) ne 'y') {
      return -1;
    }
  }

  return 0;
}

sub generateKeyfileContents($) {
  my $length = shift;
  my $password = '';
  my @normal_chars=('a'..'z','A'..'Z',0..9);
  # all printable non-alnum chars except space (0x20), backspace (0x5c),
  # and backtick (0x60)
  my @special_chars=map(chr, 0x21 .. 0x2f, 0x3a .. 0x40,
					0x5b, 0x5d .. 0x5f, 0x7b .. 0x7e);
  my $charset = join('', (@normal_chars,@special_chars));
  while (length($password) < $length) {
    $password .= substr($charset, (int(rand(length($charset)))), 1);
  }
  return $password;
}

sub generatePassword {
  my $be_silent = shift @_ || 0;
  my $password = generatePasswordFromDict($be_silent);
  if (! length($password)) {
    if (! $be_silent) {
      print color('yellow') .
	"Generated random characters instead of a words-based password.\n" .
	color('clear');
    }
    $password = generatePasswordGobbledygook(20);
  }
  return $password;
}

sub generatePasswordGobbledygook {
  my $length = shift;

  # Build the charsets that we pull from
  my @special_chars=@{$opts->{'pwsplchars'}};
  my @normal_chars=('a'..'z','A'..'Z',0..9);
  my $nc_charset = join('', @normal_chars);
  my $sc_charset = join('', @special_chars);
  my $charset = $nc_charset . $sc_charset;

  # Generate the password
  my $password = '';
  while (length($password) < $length) {
    $password .= substr($charset, (int(rand(length($charset)))), 1);
  }

  # Now we need to potentially modify the password to conform
  # with the --pwscmin and --pwscmax requirements. We do that
  # by making random substitutions of normal characters for
  # special characters or vice-versa.
  my $scmin = $opts->{pwscmin};
  my $scmax = $opts->{pwscmax};
  my $sccount = () = $password =~ m/[\Q$sc_charset\E]{1}/gi;
  SC_RANGE: until ($sccount >= $scmin && $sccount <= $scmax) {
    # Build %sc_locs and %nc_locs hashes, keyed on the
    # position of each character within $password.
    my %sc_locs = ();
    my %nc_locs = ();
    foreach my $i (0..(length($password)-1)) {
      my $char = substr($password, $i, 1);
      if ($char =~ m/^[\Q$sc_charset\E]$/) {
        $sc_locs{$i} = $char;
      } else {
        $nc_locs{$i} = $char;
      }
    }
    my $sccount = scalar(keys(%sc_locs)); # sc count in $password
    my $nccount = scalar(keys(%nc_locs)); # nc count in $password
    #print "LHHD: sccount=$sccount, nccount=$nccount, $password\n";
    #die "LHHD:\n" . Dumper(\%sc_locs, \%nc_locs) . "\n";
    if ($sccount > $scmax && $sccount > 0) { # remove a special character
      # Randomly choose a special char to replace with a normal char
      my $pos = (keys %sc_locs)[int(rand($sccount))];
      my $newchar = substr($nc_charset, (int(rand(length($nc_charset)))), 1);
      substr $password, $pos, 1, $newchar;
    } elsif ($sccount < $scmin && $nccount > 0) { # add a special character
      # Randomly choose a normal char to replace with a special char
      my $pos = (keys %nc_locs)[int(rand($nccount))];
      my $newchar = substr($sc_charset, (int(rand(length($sc_charset)))), 1);
      substr $password, $pos, 1, $newchar;
    } else {
      last SC_RANGE;
    }
    #print "  $password\n";

    # If the user asked for more special characters than the
    # entire password length, then we did our best by providing
    # nothing but special characters and so we stop here.
    if ($nccount < 1 && $scmin > length($password)) {
      last SC_RANGE;
    }
  };

  return $password
}

sub genPassInteractiveHelper($$) {
  my $mode = shift @_;
  my $len = shift @_;
  if ($mode eq 'g') {
    return generatePasswordGobbledygook($len);
  } elsif ($mode eq 'w') {
    return generatePasswordFromDict(0);
  } else {
    return undef;
  }
}

sub generatePasswordInteractive($) {
  my $default_passwd_len = shift @_;

  print "\n";
  print "INTERACTIVE PASSWORD GENERATION:\n";
  print "<n>o/<ret> Do not accept current password, generate another one.\n";
  print "<y>es      Accept current password.\n\n";
  print "<t>oggle   Toggle between random characters and word-based mode.\n";
  print "<c>ancel   Abort interactive password generation mode.\n";
  print "And in random characters mode:\n";
  print "  +/-      Increase/decrease password length. " .
				"May be prefixed with a count.\n";
  print "  [n]=     Set password length to [n] chars. If not given, " .
				"resets to $DEFAULT_PASSWD_LEN chars.\n";

  my $pw_is_ok = 0;
  my $len = $default_passwd_len;

  my $mode = 'g';
  my $pw = genPassInteractiveHelper($mode,$len);
  do {
    my $prompt_format = "%s  +/-/= n/y/t/c ";
    if ($mode eq 'w') {  $prompt_format = "%s  n/y/t/c "; }
    my $prompt = sprintf($prompt_format, $pw);
    print $prompt;
    my $input = '';
    my $input_complete = 0;
    do {
      if (recent_sigint()) { return undef; }
      my $k  = get_single_key();
      if (recent_sigint()) { return undef; }
      my $kc = unpack("C", $k);
      if ($kc == 0x03) {   # ^C
        return undef;
      } elsif ($kc == 127 || $kc == 8) { # backspace (Linux/Windows)
        if (length($input) > 0) {
          $input = substr($input,0,length($input) - 1);
          print chr(8)." ".chr(8); # Erase a character
          #print $k; # Print the backspace key to erase a character
        }
      } elsif ($kc == 0x0a) {
        $input = '';
        $input_complete = 1;
      } else {
        # Validate character input then process it
        if ($input eq '' && $k =~ m/^[tcny]$/
		|| ($mode eq 'g' && $k =~ m/^[\d\+\-=]$/ && $input =~ m/^\d*$/)
								) {
          $input .= $k;
          if ($mode eq 'g' && $input =~ /^(\d+)?[+=-]$/) {$input_complete=1;}
          if ($input =~ /^[tcny]$/ ) { $input_complete = 1; }
          if ($input =~ /^\d/) { print $k; }
        }
      }
    } while (!$input_complete);
    print "\n";

    if (lc($input) eq 't') {
      if ($mode eq 'g') { $mode = 'w' } else { $mode = 'g'; }
      $input = 'n';
    }

    if ($input eq 'y') {
      length($pw) and $pw_is_ok = 1;
    } elsif ($mode eq 'g' && $input =~ /^(\d+)?[+=-]$/) {
      my $new_len = $DEFAULT_PASSWD_LEN;
      if ($input =~ /^(\d+)?=$/) {
        $new_len = $1 || $DEFAULT_PASSWD_LEN;
      } elsif ($input =~ /^(\d+)?([+-])$/) {
        my $v = $1 ? $1 : 1;
        $v *= $2 eq '-' ? -1 : 1;
        $new_len = $len + $v;
      }
      if ($new_len < $DEFAULT_PASSWD_MIN) {
        $len = $DEFAULT_PASSWD_MIN;
      } elsif ($new_len > $DEFAULT_PASSWD_MAX) {
        $len = $DEFAULT_PASSWD_MAX;
      } else {
        $len = $new_len;
        printf "[%s%s%s]\n",
          '-' x ($len - $DEFAULT_PASSWD_MIN), '|',
          '-' x ($DEFAULT_PASSWD_MAX - $len);
      }
      if (recent_sigint()) { return undef; }
      $pw = genPassInteractiveHelper($mode,$len);
    } elsif ($input eq 'c') {
      return undef; # Return undef on cancel
    } elsif ($input eq 'n' || !$input) {
      if (recent_sigint()) { return undef; }
      $pw = genPassInteractiveHelper($mode,$len);
    }
  } while (!$pw_is_ok);
  return($pw);
}

# Inspired by http://xkcd.com/936/
sub generatePasswordFromDict($) {
  my $be_silent = shift @_ || 0;
  my @words=();
  my $fh = new FileHandle;
  my @dict_files = qw(
		/etc/dictionaries-common/words
		/usr/share/dict/words /usr/dict/words);
  if (defined($opts->{pwwords}) && length($opts->{pwwords})) {
    @dict_files = $opts->{pwwords};
  }
  DICTS: foreach my $dictfile (@dict_files) {
    if (-f $dictfile && -r $dictfile && open($fh,'<', $dictfile)) {
      @words = <$fh>;
      close($fh);
      last DICTS;
    }
  }
  if (scalar(@words) < 10000) {
    if (! $be_silent) {
      print color('yellow') .
	"No adequate dictionary found to generate a words-based password.\n".
	"These locations were checked:\n - ".join("\n - ", @dict_files)."\n" .
	"Perhaps download one from https://github.com/dwyl/english-words\n" .
	"and use the --pwwords flag.\n" .
	color('clear');
    }
    return undef;
  }
  my $length_tries = $DEFAULT_PASSWD_LEN * 2; # Scale with --pwlen
  my $password='';
  my @passwords = ();
  do {
    my $word_tries=10;
    WORD: while ($word_tries-- > 0) {
      my $word = $words[int(rand(scalar(@words)))];
      chomp $word;
      $word =~ s/[^a-zA-Z0-9]//g;
      # print "LHHD: word: $word\n";
      if (length($word) < 3) { next; } # Don't want small words
      if (length($word) > 8) { next; } # Don't want big words
      push @passwords, $word;
      last WORD; # We added a word so move on...
    }
    my $pwtmp=join('.', @passwords);
    # warn "LHHD: $pwtmp\n";
    # If we have 4 or more words and adequate length then we can exit
    if (scalar(@passwords) >= 4 && length($pwtmp) >= $DEFAULT_PASSWD_LEN) {
      $password=join('.', @passwords); # Assigning this exists the do loop
    }
  } until (length($password) || $length_tries-- < 0);

  return $password;
}

# Adapted from http://docstore.mik.ua/orelly/perl/cookbook/ch06_10.htm
sub glob2pat {
    my $globstr = shift;
    my %patmap = (
        '*' => '[^\0]*',
        '?' => '[^\0]',
        '[' => '[',
        ']' => ']',
    );
    $globstr =~ s{(.)} { $patmap{$1} || "\Q$1" }ge;
    return '^' . $globstr . '$';
}

sub shell_expansion($) {
  my $shell_path = shift @_;
  our $state;
  my $regex = glob2pat(normalize_path_string($shell_path));
  $regex = qr/$regex/;
  my @grps_and_ents = ();
  push @grps_and_ents, keys %{$state->{all_ent_paths_fwd}};
  push @grps_and_ents, keys %{$state->{all_grp_paths_fwd}};
  @grps_and_ents = sort { ncmp($a,$b); } @grps_and_ents;
  my @matches = grep(/${regex}/, @grps_and_ents);
  # Eliminate "system" things that we don't want to include
  my @good_matches = ();
  MATCHES: foreach my $match (@matches) {
    if (defined($state->{all_ent_paths_fwd}->{$match})) {
      my $ent = get_entry_by_uuid($state->{kdb}, $state->{all_ent_paths_fwd}->{$match});
      if (defined($ent) && getLabel($ent) eq 'Meta-Info' && get_username($ent) eq 'SYSTEM') {
        next MATCHES;
      }
    }
    push @good_matches, $match;
  }
  return @good_matches;
}

#########################################################################
# Setup signal handling #################################################
#########################################################################
sub setup_signal_handling {
  our $state;

  # We only worry with signal handling for Term::ReadLine::Gnu
  if ($state->{'term'}->{term}->ReadLine ne 'Term::ReadLine::Gnu') {
    return 0;
  }

  # We don't want Term::Readline::Gnu catching signals, except for WINCH.
  # I really don't understand why, but I know via experimentation.
  my $term = $state->{'term'}->{term};
  $term->Attribs->{catch_signals}  = 0;
  $term->Attribs->{catch_sigwinch} = 1; # Window resizes
  $term->clear_signals();

  # Install a signal handler to catch SIGINT (^C). Unsafe signal handling
  # (through POSIX::SigAction) is required to deal with Term::ReadLine::Gnu.
  # We don't even try for other readlines due to their limited functionality.
  my $handler_SIGINT = sub {
      our $state;
      # We could be using one of a couple of ReadLine terminals; the one
      # from Term::ShellUI ($state->{'term'}->{term}) or one from one of
      # our cli_NNN commands ($state->{active_readline}). We will assume
      # the Term::ShellUI one here, and override that below if needed.
      my $term = $state->{'term'}->{term};

      # Record in our state when a SIGINT was last received
      $state->{signals}->{INT} = [gettimeofday];

      # We need to pull the Carp longmess to see if we're sitting in a
      # a cli_XXXX function instead of at a readline prompt.
      my $mess = longmess();
      #print Dumper( $mess );
      # At some point, Term::ShellUI started wrapping my cli_XXX() routines
      # in eval{}, which hid the cli_\w+() from the longmess, and so I had
      # to add a second condition here.
      if ($mess =~ m/(main::(cli_\w+)\(|Term::ShellUI::call_cmd\()/) {
        #warn "It appears that SIGINT was called from $1\n";
        #warn "LHHD: $mess\n";
        # If the cli_NNN has an active_readline we need to work with it
        if (defined($state->{active_readline})) {
          #warn "LHHD: in INT with active_readline\n";
          my $term = $state->{active_readline};
          $term->free_line_state();
          $term->cleanup_after_signal();
          $term->reset_after_signal();
          $term->Attribs->{line_buffer}=''; # Clear the buffer
          $term->Attribs->{done}=1;  # Ask readline to return immediately
        }
      } else { # If not in a cli_XXX(), assume a Term::ShellUI prompt
        my $yellow=color('yellow');
        my $clear=color('clear');
        #$term->echo_signal_char(SIGINT); # Puts ^C on the next line. :(
        # Trial and error on these readline_state values...  :(
        #warn "LHHD: " . sprintf($term->Attribs->{readline_state}) . "\n";
        if ($term->Attribs->{readline_state} == 262374) {
          print "^C$yellow   - use Ctrl-g to stop history search.$clear\n";
        } else {
          print "^C$yellow   - use the \"quit\" command to exit.$clear\n";
        }
        $term->free_line_state();
        $term->cleanup_after_signal();
        $term->reset_after_signal();
        $term->Attribs->{line_buffer}=""; # Clear the input buffer
        $term->forced_update_display();   # Force update the display
      }
      return 0;
  };
  sigaction(SIGINT, new POSIX::SigAction($handler_SIGINT));
  #$SIG{INT} = $handler_SIGINT; # Works only if $ENV{PERL_SIGNAL}='unsafe'
  #https://groups.google.com/forum/#!topic/perl.perl5.porters/fNJdyyZh7Wc

  # Handle signal CONT - continue signal (resuming after Ctrl-Z).
  my $handler_SIGCONT = sub {
	our $state;
	my $term = $state->{'term'}->{term};
	my $mess = longmess();
               # At some point, Term::ShellUI started wrapping my cli_XXX()
               # routines in eval{}, which hid the cli_\w+() from the longmess,
               # and so I had to add a second condition here.
       if ($mess =~ m/(main::(cli_\w+)\(|Term::ShellUI::call_cmd\()/ &&
					defined($state->{active_readline})) {
	  $term = $state->{active_readline};
	}
	$term->cleanup_after_signal();
	$term->reset_after_signal();
	$term->forced_update_display(); # Force update the display
  };
  sigaction(SIGCONT, new POSIX::SigAction($handler_SIGCONT));
  #$SIG{CONT} = $handler_SIGCONT; # Works only if $ENV{PERL_SIGNAL}='unsafe'
}

# 2FA-TOTP support
sub have_otp_support() {
  if (! is_loaded('Authen::OATH')) {
    return(0, "Module Authen::OATH is required for OTP support.");
  }
  if (! is_loaded('Convert::Base32')) {
    return(0, "Module Convert::Base32 is required for OTP support.");
  }
  return(1,undef);
}
sub get_otp_data($) {
  my $ent = shift @_;

  my ($key2FA,$digest) = (undef, undef);

  # We prefer using the original, kpcli "2FA-TOTP:" style comments
  my $comment = undef;
  if (ref($state->{kdb}) eq 'File::KeePass' && defined($ent->{comment})) {
    $comment = $ent->{comment};
  } elsif (ref($ent) =~ m/^File::KDBX::/) {
    $comment = $ent->notes();
  }
  if (defined($comment)) {
    ($key2FA,$digest) = get_otp_data_from_comment($comment);
    if (defined($key2FA) && defined($digest)) {
      return ($key2FA,$digest);
    }
  }

  # If we get this far, there was no "2FA-TOTP:" style comment and so
  # we now look for a KeePassXC-style "otp" string.
  my $otpstr = undef;
  if (ref($state->{kdb}) eq 'File::KeePass' && defined($ent->{strings})) {
    if (ref($ent->{strings}) eq 'HASH' && defined($ent->{strings}->{otp})) {
      $otpstr = $ent->{strings}->{otp};
    }
  } elsif (ref($ent) =~ m/^File::KDBX::/) {
      $otpstr = $ent->string_peek("otp"); # Peek as it could be protected
  }
  if (defined($otpstr)) {
    if (! is_loaded('URI')) {
      warn "Module URI (liburi-perl) is required.\n";
    } else {
      # Parse the OTP URI
      # https://github.com/google/google-authenticator/wiki/Key-Uri-Format
      # otpauth://totp/test_entry:test%20entry%20%232? ...
      #	   ... secret=ASBFUKMNEBNZLETQ&period=30&digits=6&issuer=test_entry
      my $uri = URI->new($otpstr);
      my $up = {
	scheme    => $uri->scheme,
	authority => $uri->authority,
	path      => $uri->path,
	query     => {$uri->query_form},
	};
      #print "LHHD:\n".Dumper($otpstr, $up)."\n";
      if ($up->{scheme} ne 'otpauth') {
        print "Invalid OTP string. Expect URI format like: otpauth://.\n";
      } elsif ($up->{authority} ne 'totp') {
        print "Only authority=totp is supported: otpauth://<totp>/...\n";
      } else {
        if (defined($up->{query}) && defined($up->{query}->{secret})) {
          $key2FA = $up->{query}->{secret};
          $digest = 'SHA';
        }
      }
    }
  }

  return ($key2FA,$digest);
}
sub get_otp_data_from_comment($) {
  my $comment = shift @_;
  my @comment_lines = split(/[\r\n]+/, $comment);
  my $key2FA = undef;
  my $digest = undef;
  CLINES: foreach my $cline (@comment_lines) {
    if ($cline =~ m/^2FA-TOTP(-([^:]+))?:\s*([^\s]+)/) {
      $key2FA = $3;
      $digest = $2 || 'SHA'; # RFC6238 uses SHA-1 == Digest::SHA
      last CLINES;
    }
  }
  return($key2FA,$digest);
}

sub get_totp($$) {
  my $key2FA = shift @_ || '';
  my $digest = shift @_ || 'SHA'; # RFC6238 uses SHA-1 == Digest::SHA
  my $oath = Authen::OATH->new( digest => 'Digest::'.uc($digest) );
  my $decoded_key2FA = undef;
  $key2FA =~ s/=+$//; # Remove any trailing padding characters
  if (! eval { $decoded_key2FA = decode_base32($key2FA); }) {
    chomp $@;
    print "Failed to Base32 decode the 2FA key: $@\n";
    return undef;
  }
  my $otp = $oath->totp($decoded_key2FA);
  return $otp;
}

#########################################################################
# Setup timeout handling (--timeout=N) ##################################
#########################################################################
sub setup_timeout_handling {
  our $state;
  $state->{last_activity_time}=time;
  our $def_call_command = \&Term::ShellUI::call_command;
  if (is_loaded('Sub::Install')) {
    Sub::Install::reinstall_sub({
      into => "Term::ShellUI",
      as   => 'call_command',
      code =>
        sub {
          our $state;
          my $self = $_[0];
          my $parms = $_[1];
          my $cmd = $self->get_cname($parms->{cname});
          my $idletime = abs($state->{last_activity_time} - time);
          my $timeout_exempt=0;
          my $all_commands = $self->commands();
          if (defined($all_commands->{$cmd}) &&
		defined($all_commands->{$cmd}->{timeout_exempt}) &&
		$all_commands->{$cmd}->{timeout_exempt}) {
            $timeout_exempt=1;
          }
          if (defined($state->{kdb_file}) && length($state->{kdb_file}) &&
		($timeout_exempt == 0) && ($idletime > $opts->{timeout})) {
            print "You were idle for more than $opts->{timeout} seconds...\n";
            # GetMasterPasswd()=from user; get_master_passwd()=for kdb file
            if (GetMasterPasswd() ne get_master_passwd()) {
              print "Wrong password.\n";
              return -1;
            }
            $idletime = 0; # Reset idle time on successful password.
          }
          # Update the state->{last_activity_time} only if not already past
          # the timeout; the command could have been one one of the the
          # timeout_exempt ones, as defined in main Term::SehllUI data.
          if ($idletime <= $opts->{timeout}) {
            $state->{last_activity_time}=time;
          }
          # Call Term::ShellUI::call_command()
          our $def_call_command;
          return &$def_call_command(@_);
        },
    });
  }
}

# Code consolidation function to runtime-load optional perl modules
sub runtime_load_module {
  my $rOPTIONAL_PM = shift @_;
  my $module = shift @_;
  my $rImportList = shift @_ || [];

  my $eval_result = eval("require $module; 1;");
  if (! defined($eval_result)) { $eval_result = 0; }
  if ($eval_result == 1 && is_loaded($module)) {
    my $import_result = $module->import(@{$rImportList});
    $rOPTIONAL_PM->{$module}->{loaded} = 1;
    return 1;
  } else {
    $rOPTIONAL_PM->{$module}->{loaded} = 0;
    return 0;
  }
}

# This routine runs down the list of our preferred Term::ReadLine::*
# modules and returns a new object from the first one that we find.
sub get_readline_term {
  my $rOPTIONAL_PM = shift @_;
  my $app_name = shift @_;

  my @rl_modules = ();
  if (defined($FORCED_READLINE) && length($FORCED_READLINE)) {
    push @rl_modules, $FORCED_READLINE;
  } else {
    # The full list of readlines that we support, in order of preference
    push @rl_modules, 'Term::ReadLine::Gnu';
    push @rl_modules, 'Term::ReadLine::Perl';
    push @rl_modules, 'Term::ReadLine::Perl5';
  }
  if (lc($OSNAME) =~ m/^mswin/ && (!defined($ENV{'SHELL'}))) {
    # This supresses a diagnostics warning if/when Term::ReadLine::Perl5
    # is imported below. It tries to run '$SHELL -c "some command"' which
    # fails on windows and shows error output. The rem command will take
    # anything and return nothing, so it silences that warning.
    $ENV{'SHELL'}='rem';
  }
  # On mswin, starting with v3.5, we use Term::Size::Win32 to set the
  # COLUMNS and LINES env vars so that Term::ReadLine::Perl will stop
  # complaining about "Unable to get Terminal Size."
  if (lc($OSNAME) =~ m/^mswin/ && is_loaded('Term::Size::Win32') &&
	(! (defined($ENV{'COLUMNS'}) && defined($ENV{'LINES'})))) {
    ($ENV{'COLUMNS'}, $ENV{'LINES'}) = Term::Size::Win32::chars();
  }
  my $rl_term = undef;
  my $hold_TERM=undef;
  MODULE: foreach my $module (@rl_modules) {
    # On MS Windows, Term::ReadLine::Perl and Term::ReadLine::Perl5 are
    # pretty good terminals but they behave badly if the environment
    # variable TERM=dumb, and so we override that here if needed.
    if (lc($OSNAME) =~ m/^mswin/ && $module =~ m/^Term::ReadLine::Perl5?/ &&
			((!defined($ENV{'TERM'})) || $ENV{'TERM'} eq 'dumb')) {
      $hold_TERM=$ENV{'TERM'} || '';
      $ENV{'TERM'} = 'vt102';
    }
    if (runtime_load_module($rOPTIONAL_PM,$module,undef) eq 1) {
      # These SGI{'__WARN__'} shenanigans are to suppress:
      # WARNING: Use of inherited AUTOLOAD for non-method
      #          Term::ReadLine::Gnu::ornaments() is deprecated at
      #          /usr/lib/perl5/Term/ReadLine/Gnu.pm line 250.
      # Hopefully, newer versions of Term::ReadLine::Gnu will fix this.
      $SIG{'__WARN__'} =
		sub { warn $_[0] unless (caller eq "Term::ReadLine::Gnu"); };
      $rl_term = eval "$module->new('$app_name');";
      delete $SIG{'__WARN__'};
      last MODULE;
    } else {
      #warn "Loading $module failed\n";
      if (defined($hold_TERM)) { $ENV{'TERM'} = $hold_TERM; $hold_TERM=undef; }
    }
  }

  #if (! defined($rl_term)) { return undef; }
  if (! defined($rl_term)) {
    die "No usable Term::ReadLine::* modules found.\n" .
	"This list was tried:\n * " . join("\n * ", @rl_modules) . "\n" .
	"For more information, read the documentation: " .
					"perldoc " . basename($0) . "\n";
  }

  # I don't like readline ornaments in kpcli
  if (lc($OSNAME) =~ m/^mswin/ && is_loaded('Capture::Tiny')) {
    # On MS Windows, the RLTERM->ornaments() call causes a warning about
    # not having a termcap file. It seems hamless and so we suppress that
    # message if we have Capture::Tiny available.
    my ($out, $err, @result) = capture( sub { $rl_term->ornaments(0); } );
    if (length($err) && $err !~ m/^cannot find termcap/i) { warn $err; }
  } else {
    # WARNING: Use of inherited AUTOLOAD for non-method
    #          Term::ReadLine::Gnu::ornaments() is deprecated
    #          at line <two lines below>.
    # This "no warnings" is to stop that, but the same warning
    # still comes from Term::ReadLine::Gnu at line 250 with perl
    # v5.14.2 and Term::ReadLine::Gnu 1.20-2. That is suppressed
    # in a different way, just above in this same function.
    no warnings qw(deprecated);
    $rl_term->ornaments(0);
    use warnings qw(all);
  }

  # I'm not sure that these are only needed on Windows, but I know they
  # are not needed on Linux so I'm trying to keep the scope narrow.
  if (lc($OSNAME) =~ m/^mswin/ &&
			$rl_term->ReadLine =~ m/Term::ReadLine::Perl5?/) {
    # For Term::ReadLine::Perl and Term::ReadLine::Perl we set
    # $readline::rl_scroll_nextline=0 on MS Windows.
    if (defined($readline::rl_scroll_nextline)) {
      $readline::rl_scroll_nextline=0;
    }
    if (defined($Term::ReadLine::Perl5::readline::rl_scroll_nextline)) {
      $Term::ReadLine::Perl5::readline::rl_scroll_nextline=0;
    }
  }

  # History
  # The Term::ReadLine::Perl* modules shove values into the history
  # file automtically. That causes two problems for kpcli:
  # 1) Term::ShellUI calls $term->addhistory() itself for each CLI
  #    command that it wants to store ih history (duplicates).
  # 2) We use readline() in places like cli_new, cli_edit, etc. and
  #    we do not want all those inputs in the history file (cruft).
  if ($rl_term->ReadLine eq 'Term::ReadLine::Perl') {
    no warnings 'once';     # This is intentionally only used once
    no warnings 'redefine'; # This subrouting is intentionally redefined
    *readline::add_line_to_history = sub { return undef; };
  }
  if ($rl_term->ReadLine eq 'Term::ReadLine::Perl5') {
    no warnings 'once';     # This is intentionally only used once
    no warnings 'redefine'; # This subrouting is intentionally redefined
    *Term::ReadLine::Perl5::readline::add_line_to_history = sub {return undef;}
  }

  if (defined($hold_TERM)) { $ENV{'TERM'} = $hold_TERM; }

  return $rl_term;
}

# Use simple magic recipes to identify relevant file types
sub magic_file_type($) {
  my $filename = shift @_;
  my $header='';
  my $fh = FileHandle->new($filename, "r");
  if (defined $fh) {
    my $n = read $fh, $header, 4;
    close $fh;
  }
  # KeePass
  # Recipe from https://github.com/glensc/file/blob/master/magic/Magdir/keepass
  #0       lelong	0x9AA2D903	Keepass password database
  #>4      lelong	0xB54BFB65	1.x KDB
  #>>48    lelong	>0		\b, %d groups
  #>>52    lelong	>0		\b, %d entries
  #>>8     lelong&0x0f	1		\b, SHA-256
  #>>8     lelong&0x0f	2		\b, AES
  #>>8     lelong&0x0f	4		\b, RC4
  #>>8     lelong&0x0f	8		\b, Twofish
  #>>120   lelong	>0		\b, %d key transformation rounds
  #>4      lelong	0xB54BFB67	2.x KDBX
  if ($header =~ m/^(\x9a\xa2\xd9\x03|\x03\xd9\xa2\x9a)/) { # See SF bug #19
    return 'keepass';
  }
  # Password Safe v3
  # Recipe from https://github.com/glensc/file/blob/master/magic/Magdir/pwsafe
  if ($header =~ m/^PWS3/) {
    return 'pws3';
  }
  return ''; # Intentionally not returning undef so diagnostics won't complain
}

# https://gist.github.com/lgg/e6ccc6e212d18dd2ecd8a8c116fb1e45
sub kp_file_info {
  my $filename = shift @_;
  my $header='';
  my $fh = FileHandle->new($filename, "r");
  if (defined $fh) {
    my $n = read $fh, $header, 256; # 256 bytes is enough for KDBv1 headers
  } else {
    return undef;
  }

  use constant KP_FILE_SIG   => 0x9AA2D903;
  use constant KP_VERSIG_v1  => 0xB54BFB65;
  use constant KP_VERSIG_v2  => 0xB54BFB67;

  my ($file_sig, $ver_sig) = unpack 'LL', $header; # Two first longs from the header
  if ($file_sig != KP_FILE_SIG) {
    return undef; # Not a KeePass file
  }

  my $i = {}; # To collect our info

  # 1.x (KDB) or 2.x (KDBX)
  #>4      lelong	0xB54BFB65	1.x KDB
  #>4      lelong	0xB54BFB67	2.x KDBX
  $i->{version} = 'unknown';
  $i->{ext} = 'unknown';
  my $version_data = substr($header, 4, 4);
  #print "LHHD: version_data=" . sprintf('%v02X', $version_data) . "\n";
  if ($ver_sig == KP_VERSIG_v1) {
    $i->{version} = 1;
    $i->{ext} = 'kdb';
  } elsif ($ver_sig == KP_VERSIG_v2) {
    $i->{version} = 2;
    $i->{ext} = 'kdbx';
  } else {
    return $i;
  }

  # Parse header
  # NOTE - With KDBX4, there is no way to know for sure how
  # long the header is. With KDBv1, it's a fixed length and
  # I used to just grab 256 bytes here. That works with some
  # KDBX4 files, and not with others, and that bit me...
  my $parsed_header = undef;
  if ($i->{version} == 1) {
    $parsed_header = _parse_v1_header($header);
  } elsif ($i->{version} == 2) {
    my $more_hdr = '';
    my $n = read $fh, $more_hdr, 256*5; # Get more for KDBX files
    $header .= $more_hdr;
    $parsed_header = _parse_v2_header($header);
  }
  close $fh; # We're done reading from the file

  if (defined($parsed_header)) {
    # Add on the keys we have from above
    foreach my $k (keys %{$i}) {
      $parsed_header->{$k} = $i->{$k};
    }
    return $parsed_header;
  } else {
    return $i; # Failed to parse the header
  }
}

# Copied from File::KeePass and slightly modified
sub _parse_v1_header {
    my ($buffer) = @_;
    use constant DB_HEADSIZE_V1   => 124;
    my $size = length($buffer);
    die "File was smaller than db header ($size < ".DB_HEADSIZE_V1().")\n" if $size < DB_HEADSIZE_V1;
    my %h = (version => 1, header_size => DB_HEADSIZE_V1);
    my @f = qw(sig1 sig2 flags ver seed_rand enc_iv n_groups n_entries checksum seed_key rounds);
    my $t =   'L    L    L     L   a16       a16    L        L         a32      a32      L';
    @h{@f} = unpack $t, $buffer;

    # From https://gist.github.com/lgg/e6ccc6e212d18dd2ecd8a8c116fb1e45
    my %ciphers = (
	1 => 'SHA-256',
	2 => 'AES / Rijndael', # also know as rijndael
	4 => 'RC4',
	8 => 'Twofish',
	);
    CIPH_ID: foreach my $cipher_num (sort keys %ciphers) {
      if ($h{'flags'} & $cipher_num) {
        $h{'enc_type'} = $cipher_num;
        $h{'enc_name'} = $ciphers{$cipher_num};
      }
    }
    return \%h;
}

# Copied from File::KeePass and slightly modified by following
# this code: https://github.com/Evidlo/examples/blob/master/python/kdbx4_decrypt.py
sub _parse_v2_header {
    my ($buffer) = @_;
    #my %h = (version => 2, enc_type => 'rijndael');
    #@h{qw(sig1 sig2 ver)} = unpack 'L3', $buffer;
    my %h = (version => 2, enc_type => 'rijndael', enc_name => "AES / Rijndael");
    @h{qw(sig1 sig2 ver_min ver_maj)} = unpack 'L2 s s', $buffer;
    $h{'kdbx_ver'} = $h{ver_maj}.'.'.$h{ver_min};
    #die "Unsupported file version2 ($h{'ver'}).\n" if $h{'ver'} & 0xFFFF0000 > 0x00020000 & 0xFFFF0000;
    my $pos = 12;

    HEADER: while (1) {
        my ($type, $size);
        if ($h{ver_maj} == 3) { # KDBX3
          ($type, $size) = unpack "\@$pos CS", $buffer;
          $pos += 3;
        } elsif ($h{ver_maj} == 4) { # KDBX4
          ($type, $size) = unpack "\@$pos CL", $buffer;
          $pos += 5;
        }
        #warn "LHHD: pos/type/size = $pos: $type, $size\n";
        my $val = substr $buffer, $pos, $size; # #my ($val) = unpack "\@$pos a$size", $buffer;
        if (!$type) {
            $h{'0'} = $val;
            $pos += $size;
            last HEADER;
        }
        $pos += $size;
        if ($type == 1) {
            $h{'comment'} = $val;
        } elsif ($type == 2) {
            #warn "Cipher id did not match AES\n" if $val ne "\x31\xc1\xf2\xe6\xbf\x71\x43\x50\xbe\x58\x05\x21\x6a\xfc\x5a\xff";
            #$h{'cipher'} = 'aes';
        } elsif ($type == 3) {
            $val = unpack 'V', $val;
            warn "Compression was too large.\n" if $val > 1;
            $h{'compression'} = $val;
        } elsif ($type == 4) {
            warn "Length of seed random was not 32\n" if length($val) != 32;
            $h{'seed_rand'} = $val;
        } elsif ($type == 5) {
            warn "Length of seed key was not 32\n" if length($val) != 32;
            $h{'seed_key'} = $val;
        } elsif ($type == 6) {
            $h{'rounds'} = unpack 'L', $val;
        } elsif ($type == 7) {
            #warn "Length of encryption IV was not 16\n" if length($val) != 16;
            $h{'enc_iv'} = $val;
        } elsif ($type == 8) {
            #warn "Length of stream key was not 32\n" if length($val) != 32;
            $h{'protected_stream_key'} = $val;
        } elsif ($type == 9) {
            #warn "Length of start bytes was not 32\n" if length($val) != 32;
            $h{'start_bytes'} = $val;
        } elsif ($type == 10) {
            #warn "Inner stream id did not match Salsa20\n" if unpack('V', $val) != 2;
            $h{'protected_stream'} = 'salsa20';
        } elsif ($type == 11) {
            $h{'kdf_parameters'} = _parse_kdf_parameters($val);
            #warn "LHHD: ".Dumper($h{'kdf_parameters'})."\n";
        } elsif ($type == 12) {
            # Plugin-provided data is stored in the header field with ID 12.
        } else {
            #warn "Found an unknown header type ($type, $val)\n";
        }
    }

    $h{'header_size'} = $pos;
    return \%h;
}

# https://github.com/Evidlo/examples/blob/master/python/kdbx4_decrypt.py
# The KeePassXC source code, in ../src/format/KeePass2.cpp, contains many
# constants that we care about, such as the values for the KDF $UUID key.
sub _parse_kdf_parameters {
  my $buffer = shift @_;

  my $value_types = {
    0x04 => 'I',
    0x05 => 'Q',
    0x08 => '?',
    0x0C => 'i',
    0x0D => 'q',
    0x18 => '{length}s',
    0x42 => '{length}s',
  };

  my %h = ();
  my $kdf_offset = 0;

  my $dict_version = unpack('H', substr($buffer,0,2));
  #warn "LHHD: dict_version=$dict_version\n";
  $kdf_offset += 2;

  while (unpack('c',substr($buffer,$kdf_offset, 1)) != 0) {
    my ($value_type, $key_size) = unpack('cL<',substr($buffer,$kdf_offset));
    #warn "LHHD: value_type/format,key_size, = ($value_type/$value_types->{$value_type}, $key_size)\n";
    $kdf_offset += 1 + 4;
    my $key = substr($buffer,$kdf_offset, $key_size);
    $kdf_offset += $key_size;
    my ($value_size) = unpack('L<', substr($buffer,$kdf_offset));
    $kdf_offset += 4;
    my $value = substr($buffer,$kdf_offset, $value_size);
    $kdf_offset += $value_size;
    #warn "  LHHD: key,value_size,value = ($key, $value_size, $value)\n";
    #warn "  LHHD: key,value_size,value = ($key, $value_size, ".unpack('H*', $value)."\n";
    $h{$key} = $value;
  }

  # Convert the UUID from binary to hex and then to UUID format
  if (defined($h{'$UUID'})) {
    my $hex = lc(unpack('H*', $h{'$UUID'}));
    $h{'$UUID'} = '';
    my @lens = qw(8 4 4 4 12);
    my $offset = 0;
    foreach my $len (@lens) {
      if (length($h{'$UUID'})) { $h{'$UUID'} .= '-'; }
      $h{'$UUID'} .= substr($hex, $offset, $len);
      $offset += $len;
    }
  }
  return \%h;
}

# Dumper in a single line.
# https://metacpan.org/dist/Data-Dumper-OneLine/source/lib/Data/Dumper/OneLine.pm
sub Dumper1l {
  my $stuff = shift;
  local $Data::Dumper::Indent    = 0;
  local $Data::Dumper::Terse     = 1;
  local $Data::Dumper::Sortkeys  = 1;
  local $Data::Dumper::Quotekeys = 0;
  local $Data::Dumper::Deparse   = 1;

  # if ($Encoding) {
  #     $stuff = Data::Recursive::Encode->encode_utf8($stuff);
  # }

  my $str = Data::Dumper::Dumper($stuff); # Intentional Dumper
  $str =~ s/[\n\r]/ /g;
  return $str;
}


# Unix-style, "touch" a file
sub touch_file {
  my $filename = shift @_;
  if (! -f $filename) {
    my $fh=new FileHandle;
    open($fh, "> $filename");
    close($fh);
  }
  my $sig_pipe_store=$SIG{'PIPE'};
  $SIG{'PIPE'} = 'IGNORE';
  my $now=time;
  my $retval=utime $now, $now, $filename;
  $SIG{'PIPE'} = $sig_pipe_store;
return($retval);
}

# Convenience function to uniq an array
sub uniq {
  my %seen;
  return grep { !$seen{$_}++ } @_;
}

sub slurp_read_file {
  my $fn = shift @_;
  my $fh = FileHandle->new();
  open $fh, '<', $fn or return undef;
  local $/ = undef;
  my $data = <$fh>;
  close $fh;
  return $data;
}

# Tests to see if File::KDBX is loaded and new enough
# to be useful to us.
sub can_kdbx {
  my @errs = ();
  foreach my $module (qw(File::KDBX File::KDBX::Constants File::KDBX::Key)) {
   if (! is_loaded($module)) {
     push @errs, "$module is not loaded";
   }
  }

  my $kdbx_ver = $File::KDBX::VERSION;
  if (version->parse($kdbx_ver) < version->parse($MIN_FILE_KDBX_VER)) {
    push @errs, "File::KDBX $kdbx_ver not the minimum required version: $MIN_FILE_KDBX_VER";
  }

  my $can_kdbx = 1;
  if (scalar(@errs)) { $can_kdbx = 0; } # Cannot kdbx

  return wantarray ? @errs : $can_kdbx; # Return @errs or $can_kdbx
}

# Tests to see if the kpxc_exe command exists, is runnable,
# and is a good version versus $KPXC_MIN_VER.
sub can_kpxc {
  my $kpxc_exe = shift @_;
  my $min_ver = shift @_;
  if (! (defined($kpxc_exe) && -f -e $kpxc_exe)) { return 0; }
  {
    my $fh_kpxc = new FileHandle;
    my $cmd = "$kpxc_exe --version";
    if (lc($OSNAME) !~ m/^mswin/) { $cmd .= ' 2>/dev/null'; }
    if (! open($fh_kpxc, '-|', $cmd)) {
      return 0;
    }
    my $ver_str = <$fh_kpxc>;
    close $fh_kpxc;
    $ver_str =~ s/[\r\n]+$//;
    if ($ver_str =~ m/^(KeePassXC )?(\d+[.]\d+[.]\d+)/i) {
      my $kpxcver = $2;
      if (version->parse($kpxcver) >= version->parse($min_ver)) {
        return 1;
      }
    }
  }
  return 0;
}

###########################################################################
# Our UTF-8 related support functions, first added in April 2024 as part of
# supporting utf8 for v4.1. All of these functions should always respect
# the global $NO_UTF8 variable driven by the --noutf8 option.
###########################################################################
# Encode::decode('utf-8') a string if it isn't already utf8
sub decode_if_not_utf8 {
  my $str = shift @_;
  my $force = shift @_ // 0;
  # warn "LHHD: NO_UTF8=$NO_UTF8\n";
  return($str) if ($NO_UTF8 && !$force); # No-op under NO_UTF8 w/out force
  my $retstr = $str;
  $retstr = Encode::decode('utf-8', $retstr) if (! utf8::is_utf8($retstr));
  return $retstr;
}
# Encode::encode() a string to a perl bytestring if it is utf8
sub encode_if_utf8 {
  my $str = shift @_;
  my $force = shift @_ // 0;
  return($str) if ($NO_UTF8 && !$force); # No-op under NO_UTF8 w/out force
  my $retstr = $str;
  $retstr = Encode::encode_utf8($retstr) if (utf8::is_utf8($retstr));
  return $retstr;
}
# Helps in catching situations where ($a eq $b) comparisons happen between
# two values where one is utf8 and the other is not. Putting this into more
# places will likely help catch and fix those types of problems.
sub eq_w_utf8_check($$) {
  my $a = shift @_;
  my $b = shift @_;
  return($a eq $b) if ($NO_UTF8); # Do nothing when under NO_UTF8
  # Skip the utf8 warnings if either of the strings is zero length, else we
  # get warned about compares of empty, non-utf8 strings non-empty utf8 ones,
  # or vice-versa. Perl's eq seems to handle that case just fine so we trust
  # it and don't warn about it.
  my $do_is_utf8 = 1;
  $do_is_utf8 = 0 if (length($a) < 1);
  $do_is_utf8 = 0 if (length($b) < 1);
  # Warn if both strings have length but are utf8/non-utf8 mismatched
  if ($do_is_utf8 && int(utf8::is_utf8($a)) != int(utf8::is_utf8($b))) {
    warn "ERROR/POSSIBLE BUG: eq_w_utf8_check(\$a,\$b): utf8 eq bytestring mismatch!\n";
  }
  return($a eq $b);
}
# utf8 decode/encode all string values in an entire File::KeePass
# KDBv1 data structure (non-XML style)
# Example of what changes here on an utf8::decode():
#   "title" => "group-G\303\251n\303\251ral-3",  <-- raw from KDBv1
#   "title" => "group-G\x{e9}n\x{e9}ral-3",      <-- utf8::decode()
# Note that utf8::upgrade()/utf8::downgrade() is not correct here.
# From https://en.wikibooks.org/wiki/Perl_Programming/Unicode_UTF-8
#  - utf8::decode() may result in an N8CS byte string. That will happen when
#    the string contains *only* ASCII octets. In that case, the UTF8 flag
#    remains off and the resulting string is N8CS (Perl byte string). From the
#    testing that I have done, this seems to be just fine, but if a problem is
#    discovered, Encode::decode()/encode() could be used instead, they just do
#    not operate "in-place" like the utf:: functions do.
sub utf8_change_strings_KDBv1 {
  my $state = shift @_;
  my $action = shift @_;
  my $force = shift @_ // 0; # Default to not-forced
  die "utf8_change_strings_KDBv1(): invalid action!\n"
				if ($action !~ m/^(decode|encode)$/);
  my $k = $state->{kdb};
  my ($dc, $ec) = (0, 0);
  $dc = 1 if ($action eq 'decode'); # decode to a utf8 string
  $ec = 1 if ($action eq 'encode'); # encode to a byte string

  # This routine can only operate on KDBv1 files (File::KeePass and non-XML)
  return(undef) if (ref($k) ne 'File::KeePass'); # Not a File::KeePass DB
  return(undef) if (is_kdb_format_xml($k));      # Is a XML-style DB

  # Unless forced, we have more reasons/conditions to bail/no-op.
  # The only known reason to $force this is from mktestdb where we need this
  # subroutine to do this work on a kdb file that has not yet been save or
  # opened, and therefore the results of is_kdb_utf8_decoded() aren't valid.
  if (! $force) {
    # If we're this far we should be operating on a KDBv1 file
    # warn "LHHD: In utf8_change_strings_KDBv1() with dc=$dc/ec=$ec\n";
    return(undef) if (! $KDB1_STRS_TO_UTF8);       # Globally disabled
    return(undef) if ($dc && is_kdb_utf8_decoded($state));  # Already decoded
    return(undef) if ($ec && !is_kdb_utf8_decoded($state)); # Already encoded
  }
  #warn "LHHD: Running utf8_change_strings_KDBv1($action)\n";

  $k->unlock; # May not be needed since we don't access password

  # warn "LHHD: Acting in utf8_change_strings_KDBv1()\n";
  # Run through all groups.
  my @all_groups_flattened = $k->find_groups({});
  foreach my $g (@all_groups_flattened) {
    if ($dc && utf8::is_utf8($g->{title})) {
      warn "Trying to $action an alreaded $action-ed string\n";
    }
    utf8::decode($g->{title}) if ($dc); # In-place decode to a utf8 string
    utf8::encode($g->{title}) if ($ec); # In-place encode to a byte string
    #$g->{title} = Encode::decode('utf8',$g->{title}) if ($dc);
    #$g->{title} = Encode::encode_utf8($g->{title}) if ($ec);
  }
  # Run through all entries and every field on each one.
  # NOTES:
  #   * KDBv1 files do not have strings, thus why they are not here.
  #   * password absolutely must be a utf8 exception because File::KeePass
  #     encrypts the password fields in memory and if any of the password
  #     entries are in UTF-8 then that encryption fails.
  my @flds = qw( title url username comment tags ); # Cannot include password!
  my @all_entries_flattened = $k->find_entries({});
  foreach my $e (@all_entries_flattened) {
    foreach my $f (@flds) {
      next if (! (exists($e->{$f}) && defined($e->{$f})));
      if ($dc && utf8::is_utf8($e->{$f})) {
        warn "Trying to $action an alreaded $action-ed string\n";
      }
      utf8::decode($e->{$f}) if ($dc); # In-place decode to a utf8 string
      utf8::encode($e->{$f}) if ($ec); # In-place encode to a byte string
      #$e->{$f} = Encode::decode('utf8',$e->{$f}) if ($dc);
      #$e->{$f} = Encode::encode_utf8($e->{$f}) if ($ec);
    }
  }
  my $utf8_flag = 0;
  $utf8_flag = 1 if ($dc);
  set_kdb_utf8_decoded($state, $utf8_flag);
  $k->lock;
  #print "LHHD" .Dumper({utf8_flag=>$utf8_flag, chk=>$k->{header}->{checksum}})."\n";
}
sub is_kdbv1 {
  my $state = shift @_;
  my $k = $state->{kdb} // undef;
  return(0) if (ref($k) ne 'File::KeePass'); # Not a File::KeePass DB
  return(0) if (is_kdb_format_xml($k));      # Is a XML-style DB
  return 1; # Is a File::KeePass KDBv1 file
}
sub is_kdb_utf8_decoded {
  my $state = shift @_;
  return 0 if (! exists($state->{kdbv1_utf8_is_decoded}));
  my $kdb = $state->{kdb} // undef;
  return 0 if (! defined($kdb));
  my $hdr = $kdb->{header};
  # When we round-trip from a string (not a file), which is done in
  # cli_mktestdb, the $chk here is undef which we make an empty string.
  my $chk = $hdr->{checksum} // '';
  my $chktest = $state->{kdbv1_utf8_checksum} // '';
  if ((length($chk) || length($chktest)) && $chktest ne $chk) {
    return 0; # The kdb file is different (new one was loaded)
  }
  return $state->{kdbv1_utf8_is_decoded};
}
sub set_kdb_utf8_decoded {
  my $state = shift @_;
  my $flag = shift @_;  # 1 = utf8-decoded, 0 = not
  my $kdb = $state->{kdb} // undef;
  my $hdr = $kdb->{header};
  my $chk = $hdr->{checksum};
  $state->{kdbv1_utf8_is_decoded} = $flag;
  $state->{kdbv1_utf8_checksum} = $chk;
}
###########################################################################
###########################################################################

__END__

########################################################################
# POD ##################################################################
########################################################################

=head1 NAME

kpcli - A command line interface to KeePass database files.

=head1 DESCRIPTION

A command line interface (interactive shell) to work with KeePass
database files (http://en.wikipedia.org/wiki/KeePass).

This program was inspired by the use of "kedpm -c" combined with
the need to migrate to KeePass. The curious can read about the Ked
Password Manager at http://kedpm.sourceforge.net/.

=head1 USAGE

Please run the program and type "help" to learn how to use it.
Run the program with --help as a command line option to learn about
its command line options.

=head1 INSTALLATION

Please see https://sf.net/p/kpcli/wiki/Installation%20instructions

=head1 CAVEATS AND WORDS OF CAUTION

=head2 Supported KeePass file formats

Almost since inception, kpcli has supported KeePass v1 (*.kdb) files
and KeePass KDBX v3 (*.kdbx) files, via File::KeePass. Starting with
kpcli version 4.0, kpcli also supports KDBX v4 (*.kdbx) files and
does so via File::KDBX.

Supported formats and modules used are as follows:

  - KDB via File::KeePass
    - The original KeePass format (*.kdb)
  - KDBX3 via File::KeePass
    - The first KeePass XML format (*.kdbx v3)
  - KDBX4 via File::KDBX
    - The second KeePass XML format (*.kdbx v4)

The main author of kpcli primarily interoperability tests with KeePassX
(http://www.keepassx.org/) and primarily uses KeePass v1 (*.kdb) files.
Support for KDBX3 and KDBX4 files in kpcli is substantial, and many
people use it daily, but it is not the author's primary use case.

It is also the author's intent to maintain compatibility with v1 files,
and so anyone sending patches for consideration for inclusion in future
kpcli versions is asked to validate them with all file formats.

=head2 Filesystem Access and Tab Completion on Microsoft Windows

Filesytem access and tab completion on Microsoft Windows uses forward
slashes, and so paths like: c:/Users/hightowe/personal.kdb

File tab completion is also case insensitive, which seems cumbersome,
but it matches Windows filesystem behavior.

=head2 Some versions of Term::ReadLine::Perl5 are incompatible

C<Term::ReadLine::Perl5> versions 1.39-1.42 are incompatible with the
C<Term::ShellUI> module, which is core to kpcli. There is information about
this in kpcli SF bug #18 (http://sourceforge.net/p/kpcli/bugs/18/). The
C<Term::ReadLine::Perl5> author submitted a C<Term::ShellUI> patch to
resolve the issue (https://rt.cpan.org/Ticket/Display.html?id=105375) and
he also released C<Term::ReadLine::Perl5> version 1.43 which resolves it.

=head2 No history tracking for KDBX3 (*.kdbx) files

Recording entries' history in KDBX3 files is not implemented. History
that exists in a file is not destroyed, but results of entry changes made
in kpcli are not recorded into their history. Prior-to-change copies are
stored into the "Recycle Bin." Note that File::KeePass does not encrypt
passwords of history entries in RAM, like it does for current entries.
This is a small security risk that can, in theory, allow privileged users
to steal your passwords from RAM, from entry history.

This limitation does not exist for KDBX4 files, where File::KDBX is used.

=head2 File::KeePass bug prior to version 2.03

Prior to version 2.03, File::KeePass had a bug related to some "unknown"
data that KeePassX stores in group records. For File::KeePass < v2.03,
kpcli deletes those unknown data when saving. Research in the libkpass
(http://libkpass.sourceforge.net/) source code revealed that what early
versions of File::KeePass classifies as "unknown" are the times for
created/modified/accessed/expires as well as "flags" (id=9), but only for
groups; File::KeePass handled those fields just fine for entries.  I found
no ill-effect from dropping those fields when saving and so that is what
kpcli does to work around the File::KeePass bug, if kpcli is using
File::KeePass < v2.03.

=head1 BUGS

=head2 Using Ctrl-D to Exit

Versions of Term::ShellUI prior to v0.9. do not have the ability to trap
Ctrl-D exits by the client program. I submitted a patch to remedy that and
it made it into Term::ShellUI v0.9. Please upgrade if kpcli asks you to.

=head2 Multiple Entries or Groups With the Same Name in the Same Group

This program does not support multiple entries in the same group having
the exact same name, nor does it support multiple groups at the same
level having the same name, and it likely never will. KeepassX does
support those.  This program detects and alerts when an opened database
file has those issues, but it does not refuse to save (overwrite) a file
that is opened like that. Saves are actually safe (no data loss) as long
as the user has not touched one of the duplicately-named items.

=head2 Text::Shellwords::Cursor parse_line() infinite loop

There is a bug in Text::Shellwords::Cursor::parse_line() that will
send it into an infinite loop. To trigger it, one need only try to
do tab completion with an escape character as the last character on
the command line. This perl one-liner demonstrates the problem:

  $ perl -MData::Dumper -MText::Shellwords::Cursor \
	-e '$p=Text::Shellwords::Cursor->new(); \
	@t = $p->parse_line("open c:\\u"); print Dumper(\@t); \
	@t = $p->parse_line("open c:\\"); print Dumper(\@t);'

The second call to parse_line() will enter an infinite loop.

=head1 AUTHOR

Lester Hightower <hightowe at cpan dot org>

=head1 LICENSE

This program may be distributed under the same terms as Perl itself.

=head1 CREDITS

Special thanks to Paul Seamons, author of C<File::KeePass>, and to
Scott Bronson, author of C<Term::ShellUI>. Without those two modules
this program would not have been practical for me to author. Thanks
also to Charles McGarvey, that author of C<File::KDBX>, without
which support for the KDBX4 file format would not be possible.

=head1 CHANGELOG

 2010-Nov-28 v0.1 - Initial release.
 2010-Nov-28 v0.2 - Encrypt the master password in RAM.
 2010-Nov-29 v0.3 - Fixed master password encryption for saveas.
 2010-Nov-29 v0.4 - Fixed code to work w/out Term::ReadLine::Gnu.
                  - Documented File::KeePass v0.1 hierarchy bug.
 2010-Nov-29 v0.5 - Made find command case insensitive.
                  - Bugfix in new command (path regex problem).
 2010-Nov-29 v0.6 - Added lock file support; warn if a lock exists.
 2010-Dec-01 v0.7 - Further documented the group fields that are
                     dropped, in the CAVEATS section of the POD.
                  - Sort group and entry titles naturally.
 2010-Dec-23 v0.8 - Worked with File::KeePass author to fix a couple
                     of bugs and then required >=v0.03 of that module.
                  - Sorted "/_found" to last in the root group list.
                  - Fixed a "database changed" state bug in cli_save().
                  - Made the find command ignore entries in /Backup/.
                  - Find now offers show when only one entry is found.
                  - Provided a patch to Term::ShellUI author to add
                     eof_exit_hook and added support for it to kpcli.
 2011-Feb-19 v0.9 - Fixed bugs related to spaces in group names as
                     reported in SourceForge bug number 3132258.
                  - The edit command now prompts to save on changes.
                  - Put scrub_unknown_values_from_all_groups() calls
                     back into place after realizing that v0.03 of
                     File::KeePass did not resolve all of the problems.
 2011-Apr-23 v1.0 - Changed a perl 5.10+ regex to a backward-compatable
                     one to resolve SourceForge bug number 3192413.
                  - Modified the way that the /Backup group is ignored
                     by the find command to stop kpcli from croaking on
                     multiple entries with the same name in that group.
                     - Note: There is a more general bug here that
                             needs addressing (see BUGS section).
                  - An empty title on new entry aborts the new entry.
                  - Changed kdb files are now detected/warned about.
                  - Tested against Term::ShellUI v0.9, which has my EOF
                     hook patch, and updated kpcli comments about it.
                  - Term::ShellUI's complete_history() method was
                     removed between v0.86 and v0.9 and so I removed
                     kpli's call to it (Ctrl-r works for history).
                  - Added the "icons" command.
 2011-Sep-07 v1.1 - Empty DBs are now initialized to KeePassX style.
                  - Fixed a couple of bugs in the find command.
                  - Fixed a password noecho bug in the saveas command.
                  - Fixed a kdb_has_changed bug in the saveas command.
                  - Fixed a cli_open bug where it wasn't cli_close'ing.
                  - Fixed variable init bugs in put_master_passwd().
                  - Fixed a false warning in warn_if_file_changed().
 2011-Sep-30 v1.2 - Added the "export" command.
                  - Added the "import" command.
                  - Command "rmdir" asks then deletes non-empty groups.
                  - Command "new" can auto-generate random passwords.
 2012-Mar-03 v1.3 - Fixed bug in cl command as reported in SourceForge
                     bug number 3496544.
 2012-Apr-17 v1.4 - Added key file support based on a user contributed
                     patch with SourceForge ID# 3518388.
                  - Added my_help_call() to allow for longer and more
                     descriptive command summaries (for help command).
                  - Stopped allowing empty passwords for export.
 2012-Oct-13 v1.5 - Fixed "help <foo>" commands, that I broke in v1.4.
                  - Command "edit" can auto-generate random passwords.
                  - Added the "cls" and "clear" commands from a patch
                     with SourceForge ID# 3573930.
                  - Tested compatibility with File::KeePass v2.03 and
                     made minor changes that are possible with >=2.01.
                  - With File::KeePass v2.03, kpcli should now support
                     KeePass v2 files (*.kdbx).
 2012-Nov-25 v1.6 - Hide passwords (red on red) in the show command
                     unless the -f option is given.
                  - Added the --readonly command line option.
                  - Added support for multi-line notes/comments;
                     input ends on a line holding a single ".".
 2013-Apr-25 v1.7 - Patched to use native File::KeePass support for key
                     files, if the File::KeePass version is new enough.
                  - Added the "version" and "ver" commands.
                  - Updated documentation as Ubuntu 12.10 now packages
                     all of kpcli's dependencies.
                  - Added --histfile command line option.
                  - Record modified times on edited records, from a
                     patch with SourceForge ID# 3611713.
                  - Added the -a option to the show command.
 2013-Jun-09 v2.0 - Removed the unused Clone module after a report that
                     Clone is no longer in core Perl as of v5.18.0.
                  - Added the stats and pwck commands.
                  - Added clipboard commands (xw/xu/xp/xx).
                  - Fixed some long-standing tab completion bugs.
                  - Warn if multiple groups or entries are titled the
                     same within a group, except for /Backup entries.
 2013-Jun-10 v2.1 - Fixed several more tab completion bugs, and they
                     were serious enough to warrant a quick release.
 2013-Jun-16 v2.2 - Trap and handle SIGINT (^C presses).
                  - Trap and handle SIGTSTP (^Z presses).
                  - Trap and handle SIGCONT (continues after ^Z).
                  - Stopped printing found dictionary words in pwck.
 2013-Jul-01 v2.3 - More readline() and signal handling improvements.
                  - Title conflict checks in cli_new()/edit()/mv().
                  - Group title conflict checks in rename().
                  - cli_new() now accepts optional path&|title param.
                  - cli_ls() can now list multiple paths.
                  - cli_edit() now shows the "old" values for users
                     to edit, if Term::ReadLine::Gnu is available.
                  - cli_edit() now aborts all changes on ^C.
                  - cli_saveas() now asks before overwriting a file.
 2013-Nov-26 v2.4 - Fixed several "perl -cw" warnings reported on
                     2013-07-09 as SourceForge bug #9.
                  - Bug fix for the cl command, but in sub cli_ls().
                  - First pass at Strawberry perl/MS Windows support.
                     - Enhanced support for Term::ReadLine::Perl
                     - Added support for Term::ReadLine::Perl5
                  - Added display of expire time for show -a.
                  - Added -a option to the find command.
                  - Used the new magic_file_type() in a few places.
                  - Added generatePasswordFromDict() and "w" generation.
                  - Added the -v option to the version command.
                     - Added the versions command.
 2014-Mar-15 v2.5 - Added length control (gNN) to password generation.
                  - Added the copy command (and cp alias).
                  - Added the clone command.
                  - Added optional modules not installed to version -v.
                  - Groups can now also be moved with the mv command.
                  - Modified cli_cls() to also work on MS Windows.
                  - Suppressed Term::ReadLine::Gnu hint on MS Windows.
                  - Suppressed missing termcap warning on MS Windows.
                  - Print a min number of *s to not leak passwd length.
                  - Removed unneeded use of Term::ReadLine.
                  - Quieted "inherited AUTOLOAD for non-method" warns
                     caused by Term::Readline::Gnu on perl 5.14.x.
 2014-Jun-06 v2.6 - Added interactive password generation ("i" method).
                     - Thanks to Florian Tham for the idea and patch.
                  - Show entry's tags if present (KeePass >= v2.11).
                     - Thanks to Florian Tham for the patch.
                  - Add/edit support for tags if a v2 file is opened.
                  - Added tags to the searched fields for "find -a".
                  - Show string fields (key/val pairs) in v2 files.
                  - Add/edit for string fields if a v2 file is opened.
                  - Show information about entries' file attachments.
                     2014-03-20 SourceForge feature request #6.
                  - New "attach" command to manage file attachments.
                  - Added "Recycle Bin" functionality and --no-recycle.
                  - For --readonly, don't create a lock file and don't
                     warn if one exists. 2014-03-27 SourceForge bug #11.
                  - Added key file generation to saveas and export.
                     2014-04-19 SourceForge bug #13.
                  - Added -expired option to the find command.
                  - Added "dir" as an alias for "ls"
                  - Added some additional info to the stats command.
                  - Added more detailed OS info for Linux/Win in vers.
                  - Now hides Meta-Info/SYSTEM entries.
                  - Fixed bug with SIGTSTP handling (^Z presses).
                  - Fixed missing refresh_state_all_paths() in cli_rm.
 2014-Jun-11 v2.7 - Bug fix release. Broke the open command in 2.6.
 2015-Feb-08 v2.8 - Fixed cli_copy bug; refresh paths and ask to save.
                  - Fixed a cli_mv bug; double path-normalization.
                  - Fixed a path display bug, if done after a cli_mv.
                  - Protect users from editing in the $FOUND_DIR.
                  - Keep file opened, read-only, to show up in lsof.
                  - Added inactivity locking (--timeout parameter).
                  - Added shell expansion support to cli_ls, with the
                     ability to manage _all_ listed entries by number.
                  - Added shell expansion support to cli_mv.
                  - Added [y/N] option to list entries after a find.
 2015-Jun-19 v3.0 - Added Password Safe v3 file importing; requires
                     optional Crypt::PWSafe3 from CPAN.
                  - Added $FORCED_READLINE global variable.
                  - Attachments sanity check; SourceForge bug #17.
                  - Endianness fix in magic_file_type(); SF bug #19.
 2016-Jul-30 v3.1 - Added the purge command.
                  - Added Data::Password::passwdqc support to the
                     pwck command and prefer it over Data::Password.
                  - Minor improvements in cli_pwck().
                  - Applied SF patch #6 from Chris van Marle.
                  - Addressed items pointed out in SF patch #7.
                  - In cli_save(), worked around a File::KeePass bug.
                     - rt.cpan.org tik# 113391; https://goo.gl/v65HKE
                  - Applied SF patch #8 from Maciej Grela.
                  - Optional better RNG; SF bug #30 from Aaron Toponce.
 2017-Dec-22 v3.2 - Added xpx command per the request in SF ticket #32.
                    Added autosave functionality (shadow copies).
                    Fixed a bug in new_edit_multiline_input() that was
                     preventing blank lines between paragraphs.
                    Fixed a typo in the --help info for --pwfile.
                    Fixed a small bug in subroutine destroy_found().
 2019-Aug-16 v3.3 - Allow open and save with key-only authentication,
                     as requested in SF bug #35.
                  - Prevent "multiple entries titled" warning in the
                     /_found/ area, as reports in SF bug #36.
                  - Fix two bugs affecting Windows, as reported in
                     SourceForge patch #11.
                  - Mark /_found entries as "*OLD" when listed, if
                     they reside in a group named old. Addresses an
                     issue where searches turn up "old" accounts.
 2020-Apr-25 v3.4 - Marking of "*OLD" /_found entries now includes
                     those having any "old" group in the entire path.
                  - Added get_macos_version() and now report more
                     details for macOS in the vers command.
                  - Test for a new enough version of Clipboard if on
                     macOS 10.15.0 or newer. See SF bug #41.
                  - Added some vers reporting of a few OS-specific
                     modules (around clipboard functionality).
                  - Added the "ver -vv" and "vers -v" options, for
                     additional verbosity of version reporting.
                  - Added --pwsplchars option, as requested in
                     SourceForge feature request #19.
                  - Fixed a few new "perl -cw" warnings.
                  - Added "use diagnostics" and cleaned up some items
                     that it pointed out.
                  - Added Google Authenticator style 2FA-TOTP support,
                     and with it the otp and xo commands.
                  - Added --xpxsecs option, as requested in
                     SourceForge feature request #20.
 2020-Sep-19 v3.5 - Added --xclipsel option, in response to
                     SourceForge bug #42.
                  - Fixed inability to change fields back to empty,
                     in response to SourceForge bug #43. The problem
                     still exists for Password and Notes, but a good
                     fix for those eludes me.
                  - Support for using perl modules installed in one's
                     home directory (~/perl5) on Unix-like systems.
                  - Added KeePass v2 (*.kdbx) support to export.
                  - The show command now redacts 2FA keys in Comments
                     unless both -a and -f are specified.
                  - Fixed an issue in cli_saveas() where the *.lock
                     file from the saveas source file was stranded.
                     Also fixed not properly switching to v2 behavior
                     when saveas-ing a v1 file to v2 (*.kdb to *.kdbx).
                  - Enhanced load_lsb_release() so that it will work
                     on more Linux operating systems.
                  - Fixed a couple of "vers -v" bugs on mswin32.
                  - Fixed a couple of bugs in the stats command.
                  - Minor, non-functional changes to prevent warnings
                     in new_edit_single_line_input() and cli_pwck().
                  - Replaced checks of $OPTIONAL_PM{<foo>}->{loaded}
                     with simpler calls to is_loaded(<foo>).
                  - Added several defined() tests that "use diagnostics"
                     pointed out on an older perl that I used (v5.10.1).
 2020-Oct-14 v3.6 - Allow multiple --command parameters and execute them
                    in order, per SourceForge feature request #22.
                  - Do a cli_ls() when find returns only one result and
                    the user asks to show it. Fixes SourceForge bug #44.
                  - Added --pwscmin and --pwscmax command line options,
                    per SourceForge feature request #23.
                  - Added --nopwstars per SF feature request #24.
                  - Added --pwwords and --pwlen command line options.
                  - Word-based generated passwords respect --pwlen.
                  - Added cli_passwd() to change the DB password.
                  - Only show help message when requested by --help, not
                    also when there are command line option errors.
                  - The cd command with no specified path now goes to /.
                  - Improved open_kdb() error reporting after seeing
                    https://bugzilla.redhat.com/show_bug.cgi?id=1820134
                    and learning of the new kdbx v4 file format that
                    File::KeePass does not support.
                    Reference: https://keepass.info/help/kb/kdbx_4.html
                  - New message requesting kpcli development sponsorship.
                  - Removed the PREREQUISITES section from the POD and
                    replaced it with INSTALLATION that simply refers the
                    reader to the "Installation instructions" in the
                    kpcli project Wiki on SourceForge.
                  - Minor POD fixes.
 2022-May-19 v3.7 - Added my_complete_onlyfiles() and used it to work
                    around Term::ShellUI problems with file tab
                    completion on Windows, which now works properly.
                  - File tab completion is now case-insensitive on mswin.
                  - Now use my_complete_onlyfiles() for all platforms,
                    after discovering some other Term::ShellUI file
                    tab completion problems, even on Linux.
                  - cli_pwck() now supports Data::Password::zxcvbn and it
                    is the preferred pwck module, if it is installed.
                     - Info: https://github.com/dropbox/zxcvbn
                  - Added get_dirs() to the BEGIN block and stopped using
                    File::Find after realizing that it somewhat defeated
                    the purpose that I was trying to accomplish there.
                  - Added --nopwprint per SF bug report #44.
                  - Added the -f option to the autosave command.
                  - Fixed a --nopwstars bug per SF bug report #47.
                  - Enhanced validation of the --xclipsel option.
                  - Minor POD fixes.
                  - Added kdb_savetmp-related code to cli_save() to
                    guard against problems like the one reported in
                    Debian bug report #1006917.
 2022-Jul-21 v3.8 - Added get/set commands per SF feature request #27.
                  - Added version detection for KDBX files.
                  - Added the KDBX version in the stats output.
                  - Now reports that KDBX4 files cannot be opened.
                  - Can now import KDBX4 files using KeePassXC.
                  - Added deny_if_readonly() to import command.
 22-Jul-21 v3.8.1 - Fixed get/set commands bug. See SF feature req #27.
 2023-Aug-21 v4.0 - Added KDBX4 file format support via File::KDBX.
                  - Added the newdb and reroot commands.
                  - Added history count (Hist#) to show -a.
                  - Now supports KeePassXC-style "otp" strings for TOTP.
                  - A group can now be the target of a copy.
                  - Improved tab completion for groups and entries.
                  - Fixed a bug in open_kdb() re: saveas with --pwfile.
                  - Fixed a minor path resolution bug in cli_rmdir().
                  - Moved the BEGIN block up. Should have been done
                    that way all along, but the change was prompted by:
                    https://github.com/chazmcgarvey/File-KDBX/issues/3
                  - Modified attachment functionality per SF bug #49.
                  - Added autosave warnings when the KDB/KDBX file
                    types or extentensions do not match the master.
                  - A --pwfile file must exist or exit with error.
                  - Fixed SF bug #50 reported in kpcli-4.0-beta8.
 2024-May-23 v4.1 - Fixed SourceForge bug #51.
                  - Fixed a couple of bugs, similar to SF #51.
                  - Fixed SourceForge bug #52.
                  - Added UTF-8 support in response to SF #53.
                  - Added mktestdb and utf8 commands.
                  - Added OTP support to the set command for KDBX4.
                  - Added OTP support to the get command for KDBX4.
                  - Fixed PrintSupportMessage()-related bugs.
                  - After reroot, auto-cd to the new root group.
                  - Improved the "help find" and "help purge" messages.
                  - Allow filename parameter without --kdb=<filename>.
                  - Wrapped decode_base32() inside of get_totp() in an
                    eval() to better handle invalid Base32 strings.
 24-Sep-07 v4.1.1 - Fixed SourceForge bug #55 for perl >= 5.39.1.
 24-Sep-19 v4.1.2 - Fixed SourceForge bug #56.
 25-Jan-23 v4.1.3 - Fixed cli_save() bug for KDBv1 files.
                  - A few minor UTF-8 related bug fixes.
                  - Fixed KDBXv3 protected strings display bug, reported
                    as part of SourceForge feature request #31.
                  - Added "protection toggling" for strings, as requested
                    as part of SourceForge feature request #31.

=head1 TODO ITEMS

  Work may still be needed to support the protection of any standard
  KDBX4 strings beyond just the password, i.e. $kdbx->protect_title,
  $kdbx->protect_username, $kdbx->protect_url, $kdbx->protect_notes.
  At present, I suspect databases that have those fields set are not
  properly supported (a bug in kpcli), however, I cannot figure out
  how to make such a database in KeePassXC, so it is likely uncommon.

  Consider adding a dbsec command to allow the user to select items
  such as the Encryption Algorithm, the Key Derivation Function, the
  Transform Rounds, etc. Presently, these are respected by kpcli
  (not changed), but must be set in other tools, like KeePassXC.

  Unlike File::KeePass, File::KDBX auto-creates history records when
  entries are modified. Consider adding a command to prune history.
  Also consider auto-enforcing the $kdbx->history_max_items, the
  $kdbx->history_max_size, and the $kdbx->maintenance_history_days.
   - There are potential security implications in File::KeePass.
   - Related, consider adding a purge command for that history.

  Consider adding support for setting the Expires date/time on entries
  when creating or editing them.

  Consider enhancing pwck with these features:
    - https://metacpan.org/pod/WebService::HIBP
    - https://metacpan.org/pod/Password::Policy::Rule::Pwned
  Inspired by tools such as:
    - https://sts10.github.io/2019/02/01/medic.html
    - https://github.com/gsurrel/keepwn

  Consider adding support for TOTP with different digest algorithms
  than just SHA-1, such as SHA-256 and SHA-512. Also consider allowing
  the TOTP time to be something other than 30 seconds and the length
  of the OTP to be something other than six digits. None of those
  options are broadly used today, but when writing the TOTP code, I
  stumbled across a few. I did not implement it now primarily because
  Authen::OATH is not very condusive to using other digest algorithms.
  For future reference, would likely construct the strings like this:
    2FA-TOTP-SHA256: TheBase32SecretKeyProvided (30, 10)
  This code may prove useful if I decide to not use Authen::OATH:
  https://github.com/j256/perl-two-factor-auth/blob/master/totp.pl

  Consider adding an option related to tags within v2 files.
   - Perhaps with a --tags option to find.

  Consider adding KeePass 2.x style multi-user synchronization.

  Consider adding searches for created, modified, and accessed times
  older than a user supplied time.

=head1 OPERATING SYSTEMS AND SCRIPT CATEGORIZATION

=pod OSNAMES

=head2 Unix-like

 - Originally written and tested on Ubuntu Linux 10.04.1 LTS.
 - As of version 4.0, development is done on Linux Mint 21.1.
 - Known to work on many other Linux and *BSD distributions, and
   kpcli is packaged with many distributions now-a-days.
 - Known to work on macOS and is packaged in Homebrew (brew.sh).
 - Will use modules installed under ~/perl5/. When not given root
   permission, tools like cpanm install to ~/perl5/ by default.

=head2 Microsoft Windows

 - As of v2.4, Microsoft Windows is also supported.
 - As of v3.5, compiled on Strawberry Perl 5.32.0.1 on Windows 10.

=head2 SCRIPT CATEGORIES

=pod SCRIPT CATEGORIES

C<UNIX/System_administration>, C<Win32/Utilities>

