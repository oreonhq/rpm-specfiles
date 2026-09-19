%global source0_hash b92994727ab4a518f1326708f9cfb21b28c0bdf7ad192e36d828b2cf995a9b22

%global libraries_path %{_datadir}/beakerlib-libraries

Name: beakerlib-libraries
Version: 0.7
Release: 14%{?dist}
Summary: Beakerlib libraries

License: GPL-2.0-only
URL: https://pagure.io/beakerlib-libraries/
Source0: https://releases.pagure.org/beakerlib-libraries/%{name}-%{version}.tar.gz
BuildArch: noarch
AutoReq: no
Requires: beakerlib

%description
Beakerlib Libraries are used by beakerlib tests to encapsulate common complex
tasks such as configuring and starting a particular daemon in a single
function.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build

%install
find . -maxdepth 2 -mindepth 2 '(' -path './bin/*' -o -path './.git*' ')' -prune -o -type d \
    -exec sh -c 'install -v -d $RPM_BUILD_ROOT%libraries_path/$(dirname "{}")/Library' ';' \
    -exec sh -c 'cp -v -a "{}" $RPM_BUILD_ROOT%libraries_path/$(dirname "{}")/Library'  ';'
install -d "$RPM_BUILD_ROOT/%_bindir"
install -m755 "bin/get-test-deps" "$RPM_BUILD_ROOT/%_bindir"

%files
%libraries_path
%_bindir/get-test-deps

%changelog
%autochangelog
