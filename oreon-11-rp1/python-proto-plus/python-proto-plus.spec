%global source0_hash 5ff7ecad828e032a491fcb86947801768e32237f99dd049b649965b892ae9a63
Name:           python-proto-plus
Version:        1.28.4
Release:        1%{?dist}
Summary:        Beautiful, Pythonic protocol buffers
License:        ...
URL:            https://github.com/googleapis/google-cloud-python/tree/main/packages/proto-plus
Source0:        https://files.pythonhosted.org/packages/source/p/proto_plus/proto_plus-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-proto-plus = %{version}-%{release}
# /oreon:deps
%package -n       python3-proto-plus+testing
Summary:        Metapackage for python3-proto-plus testing extras
Requires:       python3-proto-plus = %{version}-%{release}
Requires:       python3dist(google-api-core) >= 2.25.0
Provides:       python3dist(proto-plus[testing]) = %{version}-%{release}

%description -n python3-proto-plus+testing
Metapackage for python3-proto-plus testing extras.

%description

%package -n     python3-proto-plus
Summary:        Beautiful, Pythonic protocol buffers
# oreon:reqs
Requires:       python3dist(protobuf) < 8.0.0
Requires:       python3dist(protobuf) >= 6.33.5
# /oreon:reqs
%description -n python3-proto-plus

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir proto_plus-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-proto-plus usr/lib/python3*/site-packages/proto_plus* usr/lib64/python3*/site-packages/proto_plus* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/proto_plus* usr/lib64/python3*/site-packages/proto_plus* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-proto-plus -f %{oreon_filedir}/python3-proto-plus.list

%changelog

%autochangelog
