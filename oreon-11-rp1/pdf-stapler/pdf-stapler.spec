%global source0_hash 89e1d1f102319d20e67f05225db3b6ee94c49ec18bcf098b13539595b4766678

# spec file for package pdf-stapler
#
%global commit 875325103234b4a3ed96a4a5167ff78c291edbff
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20191215

%global _description %{expand:
pdf-stapler is the Fedora package for stapler, the opensource python
project which provides a commandline tool that staples, deletes,
concatenates and shuffles documents in the Portable Document Format
(PDF). It is an alternative to PDFtk.

From the project git page:

Philip Stark found pypdf, a PDF library written in pure Python. He
couldn't find a tool which actually used the library, so he started 
writing his own.

This version of stapler is Fred Wenzel's fork of the project, with
a completely refactored source code, tests, and added functionality.}

Name:           pdf-stapler
Version:        1.0.0
Release:        0.27.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Tool for manipulating PDF documents from the command line
License:        BSD-3-Clause
URL:            https://github.com/hellerbarde/stapler
Source0:        https://github.com/hellerbarde/stapler/archive/stapler-%{commit}.tar.gz
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3-staplelib = %{version}-%{release}

%description %_description

%package -n python3-staplelib
Summary:        Module staplelib of pdf-stapler
Requires:       python3-PyPDF2

%description -n python3-staplelib %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n stapler-%{commit}
sed -i 's|"PyPDF2>=1.24"||' setup.py
# Remove upper limit from more-itertools
# https://github.com/hellerbarde/stapler/issues/71
sed -i 's|"more-itertools>=2.2,<6.0.0"|"more-itertools>=2.2"|' setup.py
# Remove shebangs from modules
sed -i -e '/^#!/d' staplelib/*.py

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
# Fedora already has a stapler package so this "stapler" package is renamed
# pdf-stapler
rm %{buildroot}%{_bindir}/stapler
%pyproject_save_files staplelib

%check
%tox

%files -n %{name}
%{_bindir}/pdf-stapler

%files -n python3-staplelib -f %{pyproject_files}
%doc README.rst
%license LICENSE

%changelog
%autochangelog
