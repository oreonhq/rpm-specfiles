%global source0_hash 97a339ce2fb0a446767ee550786e6914fa2e8cdbad39a402e48368cd0d6b5763

Summary: Fast, compact editor based on the S-Lang screen library
Name: jed
Version: 0.99.19
Release: 36%{?dist}
License: GPL-1.0-or-later
Source0: ftp://space.mit.edu/pub/davis/jed/v0.99/jed-0.99-19.tar.bz2
Patch1: jed-0.99.12-xkeys.patch
URL: http://www.jedsoft.org/jed/
Patch2: jed-etc.patch
Patch3: jed-multilib-newauto.patch
Patch4: jed-selinux.patch
Patch5: jed-verror.patch
Source1: selinux.c
Requires: slang-slsh
BuildRequires:  gcc
BuildRequires: slang-devel >= 2.0, autoconf, libselinux-devel, procps
BuildRequires: make

%description
Jed is a fast, compact editor based on the S-lang screen library.  Jed
features include emulation of the Emacs, EDT, WordStar and Brief
editors; support for extensive customization with slang macros,
colors, keybindings; and a variety of programming modes with syntax
highlighting.

You should install jed if you've used it before and you like it, or if
you haven't used any text editors before and you're still deciding
what you'd like to use.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n jed-0.99-19
%patch -P1 -p1 -b .xkeys
%patch -P2 -p1
%if "%{_lib}" == "lib64"
%patch -P3 -p1
%endif
%patch -P4 -p1 -b .selinux
%patch -P5 -p1
cp -p %{SOURCE1} src/

find doc -type f -exec chmod a-x {} \;

cd autoconf
autoconf
mv configure ..
cd ..

%build
export JED_ROOT="%{_datadir}/jed"
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

JED_ROOT=$RPM_BUILD_ROOT%{_datadir}/jed $RPM_BUILD_ROOT%{_bindir}/jed -batch -n -l preparse.sl </dev/null

# wait till jed finishes
while ps -C jed > /dev/null; do sleep 1; done

rm -f $RPM_BUILD_ROOT%{_mandir}/man*/rgrep*

rm -rf $RPM_BUILD_ROOT%{_datadir}/jed/doc/{txt,manual,README}
rm -rf $RPM_BUILD_ROOT%{_datadir}/jed/bin $RPM_BUILD_ROOT%{_datadir}/jed/info

sed -i "s|JED_ROOT|%{_datadir}/jed|g" $RPM_BUILD_ROOT/%{_mandir}/man1/jed.1

%files
%doc COPYING COPYRIGHT doc INSTALL INSTALL.unx README changes.txt
%{_bindir}/*
%{_mandir}/man1/jed.*
%{_datadir}/jed

%changelog
%autochangelog
