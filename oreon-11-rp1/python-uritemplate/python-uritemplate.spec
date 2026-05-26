%global modname uritemplate
%global altname uritemplate.py

%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        4.1.1
Release:        18%{?dist}
Summary:        Simple python library to deal with URI Templates (RFC 6570)

License:        BSD-3-Clause OR Apache-2.0
URL:            https://uritemplate.io.readthedocs
Source0:        https://github.com/sigmavirus24/%{modname}/archive/%{version}/%{modname}-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 64cae94edd83bbb0c2c49b15f2cb8192c3f8492af6bc468211d1e8b8496f5791
%global source0_file uritemplate-4.1.1.tar.gz
# oreon url source checksums end

BuildArch:      noarch

%description
%{summary}.

%package -n python3-%{modname}
Summary:        %{summary}
Conflicts:      python3-uri-templates
%{?python_provide:%python_provide python3-%{altname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest

%description -n python3-%{modname}
%{summary}.

Python 3 version.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/uritemplate-4.1.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "64cae94edd83bbb0c2c49b15f2cb8192c3f8492af6bc468211d1e8b8496f5791" || { echo "oreon: Source0 SHA256 mismatch for uritemplate-4.1.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -n uritemplate-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{modname}

%check
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
# setup.cfg declares only "LICENSE" as license file so we have to add these two
# manually
%license LICENSE.APACHE LICENSE.BSD
%doc HISTORY.rst README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.1.1-18
- Prepare for Oreon 11 (RP1)
