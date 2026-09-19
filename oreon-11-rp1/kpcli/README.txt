NAME
    kpcli - A command line interface to KeePass database files.

DESCRIPTION
    A command line interface (interactive shell) to work with KeePass
    database files (http://en.wikipedia.org/wiki/KeePass).

    This program was inspired by the use of "kedpm -c" combined with the
    need to migrate to KeePass. The curious can read about the Ked Password
    Manager at http://kedpm.sourceforge.net/.

USAGE
    Please run the program and type "help" to learn how to use it.  Run the
    program with --help as a command line option to learn about its command
    line options.

INSTALLATION
    Please see https://sf.net/p/kpcli/wiki/Installation%20instructions

CAVEATS AND WORDS OF CAUTION
Supported KeePass file formats
    Almost since inception, kpcli has supported KeePass v1 (*.kdb) files
    and KeePass KDBX v3 (*.kdbx) files, via File::KeePass. Starting with
    kpcli version 4.0, kpcli also supports KDBX v4 (*.kdbx) files and does
    so via File::KDBX.

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

Filesystem Access and Tab Completion on Microsoft Windows
    Filesytem access and tab completion on Microsoft Windows uses forward
    slashes, and so paths like: c:/Users/hightowe/personal.kdb

    File tab completion is also case insensitive, which seems cumbersome,
    but it matches Windows filesystem behavior.

Some versions of Term::ReadLine::Perl5 are incompatible
    "Term::ReadLine::Perl5" versions 1.39-1.42 are incompatible with the
    "Term::ShellUI" module, which is core to kpcli. There is information
    about this in kpcli SF bug #18
    (http://sourceforge.net/p/kpcli/bugs/18/). The "Term::ReadLine::Perl5"
    author submitted a "Term::ShellUI" patch to resolve the issue
    (https://rt.cpan.org/Ticket/Display.html?id=105375) and he also
    released "Term::ReadLine::Perl5" version 1.43 which resolves it.

No history tracking for KDBX3 (*.kdbx) files
    Recording entries' history in KDBX3 files is not implemented. History
    that exists in a file is not destroyed, but results of entry changes
    made in kpcli are not recorded into their history. Prior-to-change
    copies are stored into the "Recycle Bin." Note that File::KeePass does
    not encrypt passwords of history entries in RAM, like it does for
    current entries.  This is a small security risk that can, in theory,
    allow privileged users to steal your passwords from RAM, from entry
    history.

    This limitation does not exist for KDBX4 files, where File::KDBX is
    used.

File::KeePass bug prior to version 2.03
    Prior to version 2.03, File::KeePass had a bug related to some
    "unknown" data that KeePassX stores in group records. For File::KeePass
    < v2.03, kpcli deletes those unknown data when saving. Research in the
    libkpass (http://libkpass.sourceforge.net/) source code revealed that
    what early versions of File::KeePass classifies as "unknown" are the
    times for created/modified/accessed/expires as well as "flags" (id=9),
    but only for groups; File::KeePass handled those fields just fine for
    entries.  I found no ill-effect from dropping those fields when saving
    and so that is what kpcli does to work around the File::KeePass bug, if
    kpcli is using File::KeePass < v2.03.

BUGS
Using Ctrl-D to Exit
    Versions of Term::ShellUI prior to v0.9. do not have the ability to
    trap Ctrl-D exits by the client program. I submitted a patch to remedy
    that and it made it into Term::ShellUI v0.9. Please upgrade if kpcli
    asks you to.

Multiple Entries or Groups With the Same Name in the Same Group
    This program does not support multiple entries in the same group having
    the exact same name, nor does it support multiple groups at the same
    level having the same name, and it likely never will. KeepassX does
    support those.  This program detects and alerts when an opened database
    file has those issues, but it does not refuse to save (overwrite) a
    file that is opened like that. Saves are actually safe (no data loss)
    as long as the user has not touched one of the duplicately-named items.

Text::Shellwords::Cursor parse_line() infinite loop
    There is a bug in Text::Shellwords::Cursor::parse_line() that will send
    it into an infinite loop. To trigger it, one need only try to do tab
    completion with an escape character as the last character on the
    command line. This perl one-liner demonstrates the problem:

      $ perl -MData::Dumper -MText::Shellwords::Cursor \
            -e '$p=Text::Shellwords::Cursor->new(); \
            @t = $p->parse_line("open c:\\u"); print Dumper(\@t); \
            @t = $p->parse_line("open c:\\"); print Dumper(\@t);'

    The second call to parse_line() will enter an infinite loop.

AUTHOR
    Lester Hightower <hightowe at cpan dot org>

LICENSE
    This program may be distributed under the same terms as Perl itself.

CREDITS
    Special thanks to Paul Seamons, author of "File::KeePass", and to Scott
    Bronson, author of "Term::ShellUI". Without those two modules this
    program would not have been practical for me to author. Thanks also to
    Charles McGarvey, that author of "File::KDBX", without which support
    for the KDBX4 file format would not be possible.

CHANGELOG
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

TODO ITEMS
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

OPERATING SYSTEMS AND SCRIPT CATEGORIZATION
Unix-like
     - Originally written and tested on Ubuntu Linux 10.04.1 LTS.
     - As of version 4.0, development is done on Linux Mint 21.1.
     - Known to work on many other Linux and *BSD distributions, and
       kpcli is packaged with many distributions now-a-days.
     - Known to work on macOS and is packaged in Homebrew (brew.sh).
     - Will use modules installed under ~/perl5/. When not given root
       permission, tools like cpanm install to ~/perl5/ by default.

Microsoft Windows
     - As of v2.4, Microsoft Windows is also supported.
     - As of v3.5, compiled on Strawberry Perl 5.32.0.1 on Windows 10.

SCRIPT CATEGORIES
    "UNIX/System_administration", "Win32/Utilities"



perl v5.34.0                      2025-01-23                    KPCLI-4.1.3(1)
