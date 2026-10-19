%global source0_hash cbf11d20d518ef366878135139219dc5108ddb9679f23da80da375189a7620c9
%global debug_package   %{nil}
%global provider        github
%global provider_tld    com
%global project         TomasTomecek
%global repo            tmux-top
%global goipath         %{provider}.%{provider_tld}/%{project}/%{repo}
%global forgeurl        https://%{goipath}
%global golicenses      LICENSE
%global godocs          README.md
Version:        1.0.2
%gometa
Name:           tmux-top
Release:        1%{?dist}
Summary:        Monitoring information for your tmux status line.
License:        GPL-2.0-or-later
URL:            %{gourl}
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  make
# /oreon:deps
%description
Monitoring information for your tmux status line.

tmux-top allows you to see your:

 * load
 * memory usage
 * network information
 * I/O

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}/cmd/tmux-top
%install
%gopkginstall
install -m 0755 -vd %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/
%oreon_autofiles main

%check

export GOPATH=$(pwd):%{gopath}
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
