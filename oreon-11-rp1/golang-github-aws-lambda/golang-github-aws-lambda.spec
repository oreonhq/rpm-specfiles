%global source0_hash 5e575db971788e50bae18a57d754eb414ed2c56cd881374d22811e747745d573
%bcond check 0
%global goipath         github.com/aws/aws-lambda-go
Version:                1.55.1
%gometa
%global common_description %{expand:
Libraries, samples and tools to help Go developers develop AWS Lambda
functions.}
%global golicenses      LICENSE LICENSE-LAMBDACODE LICENSE-SUMMARY
%global godocs          README.md events/*.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Libraries, samples and tools to help Go developers develop AWS Lambda functions
License:        Apache-2.0 AND LicenseRef-Callaway-MIT
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/aws-lambda-go-%{version}.tar.gz
%if %{with check}
%endif
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  golang(github.com/stretchr/testify/assert)
BuildRequires:  golang(github.com/stretchr/testify/require)
BuildRequires:  golang(github.com/urfave/cli/v2)
# /oreon:deps
%description
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

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

%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
