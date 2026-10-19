%global source0_hash efeb16b644593e6cfdf1b5acb8789de29e56664cec3bb2ce5ce9252f28c7da8e
%global ver	1.14.9
%global snap	80b8121
%global snapver	^1.git%{snap}
Summary:        Basic library for handling email messages for Emacs
Name: flim
Version: %{ver}%{?snapver}
Release:        1%{?dist}
License: GPL-2.0-or-later
URL: https://github.com/wanderlust/flim
BuildArch: noarch
Source0:        %{name}-%{ver}-%{snap}.tar.gz
Requires: apel
# oreon:deps
BuildRequires:  apel
BuildRequires:  emacs
BuildRequires:  make
# /oreon:deps
%description
FLIM is a library to provide basic features about message
representation and encoding for Emacs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{ver}-%{snap}

%build

rm -f mailcap*
make PREFIX=$RPM_BUILD_ROOT%{_prefix} LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} PACKAGE_LISPDIR=NONE
%install
%makeinstall PREFIX=$RPM_BUILD_ROOT%{_prefix} LISPDIR=$RPM_BUILD_ROOT%{_emacs_sitelispdir} PACKAGE_LISPDIR=NONE
for i in md4 hex-util sasl-cram sasl-digest ntlm sasl sasl-ntlm hmac-def hmac-md5; do
  rm $RPM_BUILD_ROOT%{_emacs_sitelispdir}/flim/$i.el* || :
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
