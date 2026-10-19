%global source0_hash 8334da6b55d4a05dfe1492389dfe1f289953053a21773849b060d7c856ddc36e
Name:           altermime
Version:        0.3.10
Release:        1%{?dist}
Summary:        Alter MIME-encoded mailpacks
License:        LicenseRef-Callaway-BSD
URL:            http://www.pldaniels.com/altermime/
Source0:        http://www.pldaniels.com/altermime/altermime-%{version}.tar.gz
Patch0:         altermime-0.3.10-fprintf-compiler-error.patch
Patch1:         altermime-0.3.10-cflags.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
alterMIME is a small program which is used to alter MIME-encoded mailpacks.

alterMIME can:

 * Insert disclaimers
 * Insert arbitary X-headers
 * Modify existing headers
 * Remove attachments based on filename or content-type
 * Replace attachments based on filename 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p0

%build

CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS ;
make %{?_smp_mflags}
%install
rm -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 755 altermime %{buildroot}%{_bindir}/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
