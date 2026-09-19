%global source0_hash e01c26698d7fbba4fb584bb33c0d9449e2ca1f2bd371deeec0bdaf5858ca86e1

%global commit 8ea7a76324b19e0ea3b1a559cbdfb8da9d038304
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapdate 20190325

%global service extract_file

Name:           obs-service-%{service}
# Version comes from what openSUSE has released as in openSUSE:Tools
# From: https://build.opensuse.org/package/show/openSUSE:Tools/obs-service-extract_file
Version:        0.3
Release:        18%{?snapdate:.%{snapdate}git%{shortcommit}}%{?dist}
Summary:        An OBS source service: Extract a file from an archive

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch
Requires:       cpio
Requires:       bzip2
Requires:       findutils
Requires:       gzip
Requires:       tar
Requires:       unzip
Requires:       xz

%description
This is a source service for openSUSE Build Service.

It supports to extract a file from an archive, for example a spec file from a tar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -pm 0755 extract_file %{buildroot}%{_prefix}/lib/obs/service
install -pm 0644 extract_file.service %{buildroot}%{_prefix}/lib/obs/service

%files
# In lieu of a proper license file: https://github.com/openSUSE/obs-service-extract_file/issues/13
%license debian/copyright
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
%autochangelog
