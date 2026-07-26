%global source0_hash d6ea85310df6ae08e7f7e46d8b975e17fc867145ee249307413cfbe15d7121ce

Name:           b43-fwcutter
Version:        019
Release:        %autorelease
Summary:        Firmware extraction tool for Broadcom wireless driver
License:        BSD-2-Clause
URL:            https://bues.ch/b43/fwcutter/
Source0:        https://bues.ch/b43/fwcutter/%{name}-%{version}.tar.bz2
Source1:        README.too
Patch1:         b43-fwcutter-0001-fwcutter-Add-firmware-9.10.178.27.patch
Patch2:         b43-fwcutter-0002-fwcutter-make-Avoid-_DEFAULT_SOURCE-warning.patch
BuildRequires:  gcc
BuildRequires:  make

%description
This package contains the 'b43-fwcutter' tool which is used to
extract firmware for the Broadcom network devices.

See the README.too file shipped in the package's documentation for
instructions on using this tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p2

cp %{SOURCE1} .

%build
CFLAGS="$RPM_OPT_FLAGS" make

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m0755 b43-fwcutter $RPM_BUILD_ROOT%{_bindir}/b43-fwcutter
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m0644 b43-fwcutter.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/b43-fwcutter
%{_mandir}/man1/*
%license COPYING
%doc README README.too

%changelog
%autochangelog
