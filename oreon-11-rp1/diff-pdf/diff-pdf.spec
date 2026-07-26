%global source0_hash a762866df4d2c7e8827482556e812db5bff55017a7b2ec79da60c37ee70b5e88

Name:           diff-pdf
Version:        0.5.2
Release:        7%{?dist}
Summary:        A simple tool for visually comparing two PDF files

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://vslavik.github.io/diff-pdf/
Source0:        https://github.com/vslavik/diff-pdf/archive/v%{version}/diff-pdf-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  wxGTK-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  make

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
aclocal ${wx+-I} $wx -I admin
autoconf
automake --add-missing --copy --foreign
%configure --disable-silent-rules
%make_build

%install
%make_install

%files
%license COPYING COPYING.icons
%doc AUTHORS README.md
%{_bindir}/%{name}

%changelog
%autochangelog
