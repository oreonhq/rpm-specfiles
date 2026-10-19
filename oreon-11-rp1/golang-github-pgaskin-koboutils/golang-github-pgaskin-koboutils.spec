%global source0_hash 7bf1e2955185b337174a862c2c43178e6977230f926e08b387ee5e1513fcda1f
%bcond check 0
%global goipath         github.com/pgaskin/koboutils
Version:                2.1.1
%gometa
%global common_description %{expand:
Small utilities for doing stuff with Kobo eReaders.}
%global golicenses      LICENSE.md
%global godocs          README.md kobo-find.md kobo-versionextract.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Small utilities for doing stuff with Kobo eReaders
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/koboutils-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description
%{common_description}

%package -n     koboutils
Summary:        Small utilities for doing stuff with Kobo eReaders
%description -n koboutils
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
for util in kobo-find kobo-versionextract; do
  mv "${util}/README.md" "${util}.md"
done

%build

for cmd in kobo-versionextract kobo-find kobo-info; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles koboutils usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n koboutils -f %{oreon_filedir}/koboutils.list

%changelog

%autochangelog
