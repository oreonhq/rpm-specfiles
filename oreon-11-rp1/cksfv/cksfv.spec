%global source0_hash a173be5b6519e19169b6bb0b8a8530f04303fe3b17706927b9bd58461256064c

Name:           cksfv
Version:        1.3.15
Release:        16%{?dist}
Summary:        Utility to manipulate SFV files

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://gitlab.com/heikkiorsila/cksfv/
Source0:        https://zakalwe.fi/~shd/foss/%{name}/files/%{name}-%{version}.tar.bz2
Source1:        https://zakalwe.fi/~shd/foss/%{name}/files/%{name}-%{version}.tar.bz2.asc
Source2:        https://zakalwe.fi/~shd/keys/heikki-orsila-2017.pub
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires: make

%description
cksfv is a utility that can create and use SFV files. SFV (Simple File
Verification) files are used to verify file integrity using CRC32
checksums.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{S:2}' --signature='%{S:1}' --data='%{S:0}'
%setup -q

# fix rpmlint warnings
iconv -f iso8859-1 -t utf-8 ChangeLog > ChangeLog.conv &&\
touch -r ChangeLog ChangeLog.conv &&\
mv -f ChangeLog.conv ChangeLog

%build
%set_build_flags
# custom configure does not take --libdir spec
./configure \
    --bindir=%{_bindir} \
    --mandir=%{_mandir} \
    --prefix=%{_prefix} \
    --package-prefix=%{buildroot}
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog README.md TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
