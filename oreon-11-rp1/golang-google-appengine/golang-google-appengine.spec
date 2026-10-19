%global source0_hash c623d81235f7c9699e299b328191d813337dd57dcc800d7afdb5130e8c321a8f
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
%bcond check 0
%bcond_with bootstrap
%global goipath         google.golang.org/appengine
%global forgeurl        https://github.com/golang/appengine
Version:                1.6.7
%gometa
%global goipaths0       google.golang.org/appengine
%global goipathsex0     google.golang.org/appengine/blobstore
%if %{without bootstrap}
%global goipaths1       google.golang.org/appengine/blobstore
%endif
%global common_description %{expand:
This package supports the Go runtime on App Engine standard. It provides APIs
for interacting with App Engine services.}
%global golicenses      LICENSE
%global godocs          CONTRIBUTING.md README.md
%global gosupfiles glide.lock glide.yaml
Name:           %{goname}
Release:        1%{?dist}
Summary:        Go app engine packages
License:        Apache-2.0
URL:            %{gourl}
Source0:        %{forgeurl}/archive/v%{version}/appengine-%{version}.tar.gz
Source1:        glide.yaml
Source2:        glide.lock
%if %{without bootstrap}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/golang/protobuf/proto)
BuildRequires:  golang(golang.org/x/net/context)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep
cp %{S:1} %{S:2} .

%build

for cmd in cmd/* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

%if %{with bootstrap}
%gocheck -t blobstore -d internal
%else
%gocheck -d internal
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
