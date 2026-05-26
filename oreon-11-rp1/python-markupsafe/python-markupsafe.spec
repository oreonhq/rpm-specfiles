Name:           python-markupsafe
Version:        3.0.2
Release:        %autorelease
Summary:        Implements a XML/HTML/XHTML Markup safe string for Python
License:        BSD-3-Clause
URL:            https://palletsprojects.com/p/markupsafe/
Source:         https://github.com/pallets/markupsafe/archive/%{version}/markupsafe-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 cd182103704bfafefce25369fd27f14a5f578f078b7f3ddd1ce2cb940b86403a
%global source0_file markupsafe-3.0.2.tar.gz
# oreon url source checksums end

BuildRequires:  gcc
BuildRequires:  python3-devel

%global _description %{expand:
MarkupSafe implements a text object that escapes characters so it is
safe to use in HTML and XML. Characters that have special meanings are
replaced so that they display as the actual characters. This mitigates
injection attacks, meaning untrusted user input can safely be displayed
on a page.}

%description %_description


%package -n python3-markupsafe
Summary:        %{summary}

%description -n python3-markupsafe %_description


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/markupsafe-3.0.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "cd182103704bfafefce25369fd27f14a5f578f078b7f3ddd1ce2cb940b86403a" || { echo "oreon: Source0 SHA256 mismatch for markupsafe-3.0.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n markupsafe-%{version}
# Exclude C source from the package:
echo 'global-exclude *.c' >> MANIFEST.in
# Allow older setuptools
sed -i '/setuptools/s/>=.*"/"/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires requirements/tests.in


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files markupsafe


%check
%pytest


%files -n python3-markupsafe -f %{pyproject_files}
%doc CHANGES.rst README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.2-1
- Prepare for Oreon 11 (RP1)
