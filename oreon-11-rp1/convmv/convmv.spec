Summary: Convert filename encodings
Name: convmv
Version: 2.06
Release: 4%{?dist}

License: GPL-2.0-only OR GPL-3.0-only
URL: http://j3e.de/linux/convmv
Source0: http://j3e.de/linux/convmv/convmv-%{version}.tar.gz
Patch0: convmv-2.0-preserve-timestamps.patch
# oreon url source checksums begin
%global source0_sha256 a37192e266742e7fe33ec19a3be49aea7fd4d066887863a6e193fa345bf2e592
%global source0_file convmv-2.06.tar.gz
# oreon url source checksums end
BuildArch: noarch
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl(bytes)
BuildRequires: perl(Cwd)
BuildRequires: perl(Encode)
BuildRequires: perl(File::Basename)
BuildRequires: perl(File::Compare)
BuildRequires: perl(File::Find)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Unicode::Normalize)
BuildRequires: perl(utf8)

%description
This package contains the tool convmv with which you can convert the encodings
of filenames, e.g. from Latin1 to UTF-8.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/convmv-2.06.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a37192e266742e7fe33ec19a3be49aea7fd4d066887863a6e193fa345bf2e592" || { echo "oreon: Source0 SHA256 mismatch for convmv-2.06.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q
%patch 0 -p1 -b .preserve-timestamps
tar -xf testsuite.tar

%build
make %{_smp_mflags}

%check
make test

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install

%files
%doc CREDITS Changes TODO
%license GPL2
%{_bindir}/convmv
%{_mandir}/man*/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.06-4
- Prepare for Oreon 11 (RP1)
