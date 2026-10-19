%global source0_hash 16910b594704b40e9df35eb3bc637db675fe3d770a4588bd32b5a12c5ff174ff
%bcond check 0
%global goipath         github.com/schollz/croc
Version:                11.5.4
%gometa -f
%global goaltipaths     github.com/schollz/croc/v9
%global common_description %{expand:
croc is a tool that allows any two computers to simply and securely transfer
files and folders.}
%global golicenses      LICENSE
%global godocs          README.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Easily and securely send things from one computer to another
License:        MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/croc-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%package -n       croc
Summary:        Easily and securely send things from one computer to another
BuildArch:      noarch

%description -n croc
Easily and securely send things from one computer to another

%description %{common_description}

%package -n     croc
Summary:        Easily and securely send things from one computer to another
%description -n croc
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%autopatch -p1

%build

%gobuild -o %{gobuilddir}/bin/croc %{goipath}
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
install -Dpm0644 -t %{buildroot}%{_unitdir} croc.service
install -Dpm0644 src/install/bash_autocomplete \
                 %{buildroot}%{bash_completions_dir}/croc
install -Dpm0644 src/install/zsh_autocomplete \
                 %{buildroot}%{zsh_completions_dir}/_croc
%oreon_autofiles croc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with check}
%check

skip="TestPublicIP"
%if 0%{?fc38}
%ifarch s390x
skip="$skip TestSend"
%endif
%endif
for test in $skip \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%post

%systemd_post croc.service
%preun

%systemd_preun croc.service
%postun

%systemd_postun_with_restart croc.service
%files -f %{oreon_filedir}/main.list
%files -n croc -f %{oreon_filedir}/croc.list

%changelog

%autochangelog
