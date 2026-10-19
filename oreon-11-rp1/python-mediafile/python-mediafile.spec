%global source0_hash 80c9003fd25d7096a7237e3b58e6ff018ef67f9c39900feafacabac1742c7d3a
Name:           python-mediafile
Version:        0.17.0
Release:        1%{?dist}
Summary:        A simple, cross-format library for reading and writing media file metadata.
License:        MIT
URL:            https://github.com/beetbox/mediafile
Source0:        https://files.pythonhosted.org/packages/source/m/mediafile/mediafile-%{version}.tar.gz
BuildArch:      noarch
Patch0:         0001-Set-new-ORIGINALDATE-tag-for-m4a-files-in-addition-t.patch
Patch1:         0002-Version-bump-changelog-for-71.patch
Patch2:         0003-remove-usage-of-six-__future__.patch
Patch3:         0004-Changelog-for-72.patch
Patch4:         0005-Bump-minimum-Python-versions.patch
Patch5:         49da9728a69ae8a63af8a4630fccc55c10e66392-nobinary.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-mediafile = %{version}-%{release}
# /oreon:deps
%package -n       python3-mediafile+docs
Summary:        Metapackage for python3-mediafile docs extras
Requires:       python3-mediafile = %{version}-%{release}
Requires:       python3dist(sphinx) >= 7.4.7
Provides:       python3dist(mediafile[docs]) = %{version}-%{release}

%description -n python3-mediafile+docs
Metapackage for python3-mediafile docs extras.

%description

%package -n     python3-mediafile
Summary:        A simple, cross-format library for reading and writing media file metadata.
# oreon:reqs
Requires:       python3dist(filetype) >= 1.2.0
Requires:       python3dist(mutagen) >= 1.46
# /oreon:reqs
%description -n python3-mediafile

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir mediafile-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-mediafile usr/lib/python3*/site-packages/mediafile* usr/lib64/python3*/site-packages/mediafile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/mediafile* usr/lib64/python3*/site-packages/mediafile* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-mediafile -f %{oreon_filedir}/python3-mediafile.list

%changelog

%autochangelog
