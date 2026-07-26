%global source0_hash f0d9c19b79bb8e66a7111e481452cdb416ce474e4d02e58d698383c03c6a7e3f

Summary:       Perl backend for Qooxdoo
Name:          perl-qooxdoo-compat
Version:       0.7.3
Release:       51%{?dist}
License:       LGPL-2.0-or-later OR EPL-1.0
URL:           http://qooxdoo.org/
Source0:       http://downloads.sourceforge.net/qooxdoo/qooxdoo-%{version}-backend.tar.gz
Patch0:        perl-qooxdoo-compat-0.7.3-strict.patch
BuildArch:     noarch
BuildRequires: perl-generators

%description
This package provides the Perl backend for Qooxdoo, a comprehensive
and innovative Ajax application framework. This package supports
Qooxdoo 0.7.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n qooxdoo-%{version}-backend

%build
# nothing to build

%install
install -Dp -m 0644 backend/perl/Qooxdoo/JSONRPC.pm \
    %{buildroot}%{perl_vendorlib}/Qooxdoo/JSONRPC.pm

%files
%license LICENSE
%doc AUTHORS README RELEASENOTES TODO VERSION
%{perl_vendorlib}/Qooxdoo

%changelog
%autochangelog
