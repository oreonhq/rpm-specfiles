%global source0_hash a762866df4d2c7e8827482556e812db5bff55017a7b2ec79da60c37ee70b5e88
Name:           diff-pdf
Version:        0.5.2
Release:        1%{?dist}
Summary:        A simple tool for visually comparing two PDF files
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://vslavik.github.io/diff-pdf/
Source0:        https://github.com/vslavik/diff-pdf/archive/v%{version}/diff-pdf-%{version}.tar.gz
# oreon:deps
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  poppler-glib-devel
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

aclocal ${wx+-I} $wx -I admin
autoconf
automake --add-missing --copy --foreign
%configure --disable-silent-rules
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
