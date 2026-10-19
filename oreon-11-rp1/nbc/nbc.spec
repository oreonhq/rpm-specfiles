%global source0_hash 6104ce4124c064332dab70c4c3bfd9d81254ff1f1ed49fbaf0fdbcfc39aa4ce8
Name:           nbc
Version:        1.2.1.r3
Release:        1%{?dist}
Summary:        Simple language and compiler to program the LEGO NXT brick
URL:            http://bricxcc.sourceforge.net/nbc/
License:        LicenseRef-Callaway-MPLv1.1
Source0:        http://downloads.sourceforge.net/bricxcc/%{name}-%{version}.src.tgz
Patch0:         %{name}-1.2.1.r3.fixinstall.patch
ExclusiveArch:  %{fpc_arches}
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  fpc
BuildRequires:  glibc-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  make
# /oreon:deps
%description
Next Byte Codes (NBC) is a simple language with an assembly language
syntax that can be used to program LEGO's NXT programmable brick
(from the new LEGO Mindstorms NXT set).

Not Exactly C (NXC) is a high level language, similar to C, built on
top of the NBC compiler. It can also be used to program the NXT brick.
NXC is basically NQC (Not Quite C) for the NXT.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c -q
%patch -P0 -p0 -b .fixinstall

cd doc
for f in Readme Changelog; do
  dos2unix -n $f $f.tmp && \
  touch -r $f $f.tmp && \
  mv $f.tmp $f
done

%build

make
%install
make install DISTDIR=%{buildroot}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
