%global source0_hash 4c5c6136540384e5455b250f768e7ca11b03fdba1a8efc2341ee0f1111e57612

Name:     scdoc
Version:  1.11.3
Release:  %autorelease
Summary:  Tool for generating roff manual pages

License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:  %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc
BuildRequires: sed

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Disable static linking
sed -i '/-static/d' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

%build
make PREFIX=%{_prefix} %{?_smp_mflags}

%install
%if 0%{?el7}
%make_install PREFIX=%{_prefix} INSTALL="%{__install} -p"
%else
%make_install PREFIX=%{_prefix}
%endif

%check
make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
# Not shipped in a -devel package since scdoc is a development tool not
# installed in a user runtime.
%{_datarootdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
