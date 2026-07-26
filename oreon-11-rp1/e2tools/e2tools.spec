%global source0_hash c1a06b5ae2cbddb6f04d070e889b8bebf87015b8585889999452ce9846122edf

Name:           e2tools
Version:        0.1.0
Release:        15%{?dist}
Summary:        Manipulate files in unmounted ext2/ext3 filesystems

# No version specified.
License:        GPL-1.0-or-later
URL:            https://e2tools.github.io/
Source0:        https://github.com/e2tools/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  e2fsprogs-devel >= 1.27
BuildRequires:  libcom_err-devel

BuildRequires:  e2fsprogs
BuildRequires: make

%description
A simple set of utilities to read, write, and manipulate files in an
ext2/ext3 filesystem directly using the ext2fs library. This works

  - without root access
  - without the filesystem being mounted
  - without kernel ext2/ext3 support

The utilities are: e2cp e2ln e2ls e2mkdir e2mv e2rm e2tail

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -v

%build
%configure
%{__make} %{?_smp_mflags}

%check
%{__make} %{?_smp_flags} check

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS
%doc COPYING
%doc ChangeLog
%doc NEWS.md
%doc README.md
%doc TODO

%{_bindir}/e2tools
%doc %{_mandir}/man7/e2tools.7.gz

%{_bindir}/e2cp
%doc %{_mandir}/man1/e2cp.1.gz

%{_bindir}/e2ln
%doc %{_mandir}/man1/e2ln.1.gz

%{_bindir}/e2ls
%doc %{_mandir}/man1/e2ls.1.gz

%{_bindir}/e2mkdir
%doc %{_mandir}/man1/e2mkdir.1.gz

%{_bindir}/e2mv
%doc %{_mandir}/man1/e2mv.1.gz

%{_bindir}/e2rm
%doc %{_mandir}/man1/e2rm.1.gz

%{_bindir}/e2tail
%doc %{_mandir}/man1/e2tail.1.gz

%changelog
%autochangelog
