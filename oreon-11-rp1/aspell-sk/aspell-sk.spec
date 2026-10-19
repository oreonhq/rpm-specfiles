%global source0_hash 9e229dd24df0819b5fc9a78c23877f4b88462f6702e79fbfecd6ad39a7380d43
%define aspellversion 6
%define lang sk
%define langrelease 1
%define aspellname aspell%{aspellversion}-%{lang}
Name:           aspell-%{lang}
Version:        2.4.7
Release:        1%{?dist}
Summary:        Slovak dictionaries for Aspell
License:        GPL-2.0-only OR LicenseRef-Callaway-LGPLv2 OR LicenseRef-Callaway-MPLv1.1
URL:            http://sk-spell.sk.cx/aspell-sk
Source0:        http://www.%{lang}-spell.%{lang}.cx/files/%{aspellname}-%{version}-%{langrelease}.tar.bz2
Provides:  deprecated()
Requires:       aspell >= 12:0.60
%define debug_package %{nil}                                                    
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Slovak

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{aspellname}-%{version}-%{langrelease}

%build

sh configure
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
