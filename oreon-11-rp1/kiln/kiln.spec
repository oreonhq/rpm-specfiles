%global source0_hash 6de055814c7f363c2b5e358dcbed4ca010ca2c11c887b7e506f1574b68f1dd88
%bcond check 0
%global goipath         git.sr.ht/~adnano/kiln
%global forgeurl        https://git.sr.ht/~adnano/kiln
Version:                0.4.0
%global tag             0.4.0
%global repo            kiln
%global archivename     %{repo}-%{tag}
%global archiveext      tar.gz
%global archiveurl      %{forgeurl}/archive/%{tag}.%{archiveext}
%global topdir          %{repo}-%{tag}
%global extractdir      %{repo}-%{tag}
%global scm             git
%gometa
%global common_description %{expand:
A simple static site generator.
Features
 - Simple
 - Extensible
 - Gemini support
 - Atom feeds
 - Go templates}
Name:           kiln
Release:        1%{?dist}
Summary:        Simple static site generator.
License:        MIT
URL:            %{gourl}
Source0:        %{archiveurl}#/%{archivename}.%{archiveext}
Patch0:         kiln-fix-makefile.patch
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang
BuildRequires:  scdoc
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
%patch -P0 -p1

%build

export LDFLAGS="-X main.Version=%{version} "
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}
%make_build docs
%install
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
export PREFIX=%{_prefix}
%make_install
%oreon_autofiles main
%if %{with check}
%check

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
