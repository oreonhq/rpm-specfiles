%global source0_hash 12024ed0785beb223d183d83ac730c47529556ac394536d889c7fd6210232a22
%bcond check 0
%global goipath         github.com/schollz/mnemonicode
Version:                1.0.1
%global commit          63fa713ece0d70791ffb132af953d09856d57d4f
%gometa -f
%global common_description %{expand:
Mnemonicode is a method for encoding binary data into a sequence of words which
can be spoken over the phone, for example, and converted back to data on the
other side.}
%global golicenses      LICENCE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Method for encoding binary data into a sequence of words
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/%{commit}/mnemonicode-%{commit}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
# /oreon:deps
%description %{common_description}

%package -n     mnemonicode
Summary:        Method for encoding binary data into a sequence of words
License:        LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
%description -n mnemonicode
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles mnemonicode usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list
%files -n mnemonicode -f %{oreon_filedir}/mnemonicode.list

%changelog

%autochangelog
