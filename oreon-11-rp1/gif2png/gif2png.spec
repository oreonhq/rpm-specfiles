%global source0_hash f7584dc0d15b8186182e47dcf6190924a3ba6d669acfce33be8512a79ae6fe20

%global debug_package %{nil}

Summary:	A GIF to PNG converter
Name:		gif2png
Version:	2.5.14
Release:	%autorelease
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		http://www.catb.org/~esr/gif2png/
Source0:	http://www.catb.org/~esr/gif2png/%name-%version.tar.gz
Source100:	test-0.gif
Source101:	test-1.gif
BuildRequires:  gcc
BuildRequires:	libpng-devel
BuildRequires:	make

%description
The gif2png program converts files from the obsolescent Graphic Interchange
Format to Portable Network Graphics. The conversion preserves all graphic
information, including transparency, perfectly. The gif2png program can
even recover data from corrupted GIFs.

There exists a 'web2png' program in a separate package which is able
to convert entire directory hierarchies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%make_build

%install
%make_install

# web2png is Python 2 only, see https://bugzilla.redhat.com/show_bug.cgi?id=1787242
rm %{buildroot}%{_bindir}/web2png
rm %{buildroot}%{_mandir}/man1/web2png*

#disable tests for while
#%check
#P=./gif2png
#for i in %SOURCE100 %SOURCE101; do
#    rm -f _tmp.gif
#    install -p -m 0644 $i _tmp.gif
#    $P _tmp.gif
#    $P -f < "$i" > _tmp.png
#    $P -O -f < "$i" > _tmp.png
#done

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}*

%changelog
%autochangelog
