%global source0_hash 0b83f8698dd8ef44ca97b25c4748c087133f53c7fff39b6b70dab65931def8b0

Summary:          Re-implementation for Unix of the Plan 9 shell
Name:             rc
Version:          1.7.4
Release:          27%{?dist}
License:          Zlib
URL:              https://github.com/rakitzis/rc
Source0:          https://github.com/rakitzis/rc/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:           https://github.com/rakitzis/rc/commit/429f81caf8af998e59075c86b777b2ecef7956cf.patch#/rc-1.7.4-c23.patch
Conflicts:        filesystem < 3
Provides:         /bin/rc
Requires(post):   grep
Requires(postun): sed
BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    gcc
BuildRequires:    make
BuildRequires:    readline-devel

%description
Rc is a command interpreter for Plan 9 that provides similar facilities to
UNIX's Bourne shell, with some small additions and less idiosyncratic syntax.
This is a re-implementation for Unix, by Byron Rakitzis, of the Plan 9 shell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
autoreconf --force --install

%build
%configure --with-edit=gnu
%make_build

%install
%make_install

%check
make check

%post
grep -q "^/bin/%{name}$" %{_sysconfdir}/shells 2>/dev/null || \
  echo "/bin/%{name}" >> %{_sysconfdir}/shells
grep -q "^%{_bindir}/%{name}$" %{_sysconfdir}/shells 2>/dev/null || \
  echo "%{_bindir}/%{name}" >> %{_sysconfdir}/shells

%postun
if [ ! -x %{_bindir}/%{name} ]; then
  sed -e 's@^/bin/%{name}$@POSTUNREMOVE@' -e '/^POSTUNREMOVE$/d' -i %{_sysconfdir}/shells
  sed -e 's@^%{_bindir}/%{name}$@POSTUNREMOVE@' -e '/^POSTUNREMOVE$/d' -i %{_sysconfdir}/shells
fi

%files
%license COPYING
%doc ChangeLog AUTHORS EXAMPLES NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
