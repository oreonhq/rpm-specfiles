%global source0_hash cf18a8c52138a38541be3478af446c06048108729d7e18476492d62d54baabc4

Name:           libeatmydata
Version:        131
Release:        3%{?dist}
Group:          Development/Tools
# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
Summary:        Library and utilities designed to disable fsync and friends
BuildRequires:  gcc, make, libtool, strace, gnupg
Source0:        https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz
Source1:        https://www.flamingspork.com/projects/libeatmydata/%{name}-%{version}.tar.gz.asc
Source2:        https://flamingspork.com/stewart.gpg
# Man page to be included upstream soon...
Source3:        https://salsa.debian.org/debian/libeatmydata/-/raw/048c4ea3/debian/eatmydata.1

URL:            https://www.flamingspork.com/projects/libeatmydata/
%if !(0%{?rhel} && 0%{?rhel} < 8)
Recommends: eatmydata
%endif

%description
This package contains a small LD_PRELOAD library (libeatmydata) and a couple 
of helper utilities (eatmydata) designed to transparently disable fsync and
friends (like open(O_SYNC)). This has two side-effects: making software that
writes data safely to disk a lot quicker and making this software no longer 
crash safe.

%package -n eatmydata
Summary: Utility to disable fsync() and friends for the command specified 
# Explict requires as the main package is a shell script that does an LD_PRELOAD
# and thus we don't get automatic dependencies!
Requires: %{name}

%description -n eatmydata
The eatmydata script does the heavy lifting of LD_PRELOAD for the command
specified. You can also symlink a command to the eatmydata wrapper and the
wrapper will find the command in PATH and then execute it after setting up
the libeatmydata LD_PRELOAD

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%configure --enable-static=no
%make_build

%install

%make_install
mkdir -p %{buildroot}%{_mandir}/man1/
install -m444 -p %{SOURCE3} %{buildroot}%{_mandir}/man1/

%if !0%{?fedora} || 0%{?fedora} < 36
find %{buildroot} -name "*.la" -type f -delete
%endif

%check
%{__make} check

%files -n eatmydata
%{_bindir}/eatmydata
%{_libexecdir}/eatmydata.sh
%{_mandir}/man1/eatmydata.1*
%doc README.md AUTHORS
%license COPYING

%files
%{_libdir}/*.so

%changelog
%autochangelog
