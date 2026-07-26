%global source0_hash f8e7a2f523c9253531b632ee9f8ac2ecb48226987c0ac1d52f33d8334fa80b07

Name:           rpmreaper
Version:        0.2.0
Release:        37%{?dist}
Summary:        A tool for removing packages from system

License:        GPL-2.0-or-later
URL:            https://github.com/mlichvar/rpmreaper
Source0:        https://github.com/mlichvar/rpmreaper/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         rpmreaper-provfilename.patch
Patch2:         rpmreaper-warnings.patch

BuildRequires: make
BuildRequires:  gcc ncurses-devel rpm-devel
Requires:       less rpm

%description
rpmreaper is a simple ncurses application with a mutt-like interface that
allows removing unnecessary packages and their dependencies from the system.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P1 -p1 -b .provfilename
%patch -P2 -p1 -b .warnings

%build
make %{?_smp_mflags} EXTRA_CFLAGS="$RPM_OPT_FLAGS"

%install
%makeinstall

%files
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
