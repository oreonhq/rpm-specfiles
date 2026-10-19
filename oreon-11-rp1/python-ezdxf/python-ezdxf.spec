%global source0_hash da5a5e0e6bdbb6656f9c017b47edc7eafceb419d61a2b5de64ffb344c168e593
Name:           python-ezdxf
Version:        1.4.4
Release:        1%{?dist}
Summary:        A Python package to create/manipulate DXF drawings.
License:        MIT
URL:            https://github.com/mozman/ezdxf
Source0:        https://files.pythonhosted.org/packages/source/e/ezdxf/ezdxf-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ezdxf = %{version}-%{release}
# /oreon:deps
%package -n       python3-ezdxf+draw
Summary:        Metapackage for python3-ezdxf draw extras
Requires:       python3-ezdxf = %{version}-%{release}
Requires:       python3dist(pymupdf) >= 1.20.0
Provides:       python3dist(ezdxf[draw]) = %{version}-%{release}

%description -n python3-ezdxf+draw
Metapackage for python3-ezdxf draw extras.

%package -n       python3-ezdxf+draw5
Summary:        Metapackage for python3-ezdxf draw5 extras
Requires:       python3-ezdxf = %{version}-%{release}
Requires:       python3dist(pymupdf) >= 1.20.0
Provides:       python3dist(ezdxf[draw5]) = %{version}-%{release}

%description -n python3-ezdxf+draw5
Metapackage for python3-ezdxf draw5 extras.

%package -n       python3-ezdxf+dev
Summary:        Metapackage for python3-ezdxf dev extras
Requires:       python3-ezdxf = %{version}-%{release}
Requires:       python3dist(pymupdf) >= 1.20.0
Provides:       python3dist(ezdxf[dev]) = %{version}-%{release}

%description -n python3-ezdxf+dev
Metapackage for python3-ezdxf dev extras.

%package -n       python3-ezdxf+dev5
Summary:        Metapackage for python3-ezdxf dev5 extras
Requires:       python3-ezdxf = %{version}-%{release}
Requires:       python3dist(pymupdf) >= 1.20.0
Provides:       python3dist(ezdxf[dev5]) = %{version}-%{release}

%description -n python3-ezdxf+dev5
Metapackage for python3-ezdxf dev5 extras.

%description

%package -n     python3-ezdxf
Summary:        A Python package to create/manipulate DXF drawings.
# oreon:reqs
Requires:       python3dist(pyparsing) >= 3.0.0
Requires:       python3dist(typing-extensions) >= 4.6.0
# /oreon:reqs
%description -n python3-ezdxf

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir ezdxf-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-ezdxf usr/lib/python3*/site-packages/ezdxf* usr/lib64/python3*/site-packages/ezdxf* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/ezdxf* usr/lib64/python3*/site-packages/ezdxf* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-ezdxf -f %{oreon_filedir}/python3-ezdxf.list

%changelog

%autochangelog
