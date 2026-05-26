%global pypi_name lesscpy

%if 0%{?rhel} > 7
# Disable python2 build by default
%endif

Name:           python-%{pypi_name}
Version:        0.14.0
Release:        24%{?dist}
Summary:        Lesscss compiler

License:        MIT
URL:            https://github.com/robotis/lesscpy
Source0:        https://pypi.python.org/packages/source/l/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Patch1:         0001-Remove-tabfile-support-as-PLY-removed-it-as-well.patch
# oreon url source checksums begin
%global source0_sha256 7b664f60818a16afa8cc9f1dd6d9b17f944e0ce94e50787d76f81bc7a8648cce
%global source0_file lesscpy-0.14.0.tar.gz
# oreon url source checksums end

BuildArch:      noarch
 
%global _description\
A compiler written in python 3 for the lesscss language.  For those of us not\
willing/able to have node.js installed in our environment.  Not all features\
of lesscss are supported (yet).  Some features wil probably never be\
supported (JavaScript evaluation).

%description %_description


%package -n python3-lesscpy
Summary:    %summary
Requires:   python3-ply
Requires:   python3-six
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-ply
BuildRequires: python3-pytest
BuildRequires: python3-six
%{?python_provide:%python_provide python3-lesscpy}

%description -n python3-lesscpy
A compiler written in python 3 for the lesscss language.  For those of us not
willing/able to have node.js installed in our environment.  Not all features
of lesscss are supported (yet).  Some features wil probably never be
supported (JavaScript evaluation).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/lesscpy-0.14.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7b664f60818a16afa8cc9f1dd6d9b17f944e0ce94e50787d76f81bc7a8648cce" || { echo "oreon: Source0 SHA256 mismatch for lesscpy-0.14.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n %{pypi_name}-%{version}

%build

%py3_build


%install

%py3_install
# link for backwards compatibility. consider removal in Fedora 30+
ln -s ./lesscpy %{buildroot}/%{_bindir}/py3-lesscpy


%check
%pytest


%files -n python3-lesscpy
%doc LICENSE
%{_bindir}/lesscpy
%{_bindir}/py3-lesscpy
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}*.egg-info


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.0-24
- Prepare for Oreon 11 (RP1)
