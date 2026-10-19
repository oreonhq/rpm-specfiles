%global source0_hash 89d4b530c394313cc3f3a4e07a7394fa82a6091f44df44dfcd0ebcb3300a81de
Name:           toilet
Version:        0.3
Release:        1%{?dist}
Summary:        Display large colorful characters in text mode
License:        WTFPL
URL:            http://caca.zoy.org/wiki/toilet
Source0:        http://caca.zoy.org/raw-attachment/wiki/%{name}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcaca-devel
BuildRequires:  make
# /oreon:deps
%description
The TOIlet project attempts to create a free replacement for the FIGlet
utility. TOIlet stands for "The Other Implementation’s letters", coined after
FIGlet's "Frank, Ian and Glen’s letters".

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
