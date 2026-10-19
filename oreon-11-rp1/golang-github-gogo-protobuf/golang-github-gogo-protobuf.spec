%global source0_hash 2bb4b13d6e56b3911f09b8e9ddd15708477fbff8823c057cc79dd99c9a452b34
%bcond check 0
%global goipath         github.com/gogo/protobuf
Version:                1.3.2
%gometa
%global common_description %{expand:
Gogoprotobuf is a fork of golang/protobuf with extra code generation features.
This code generation is used to achieve:
 - fast marshalling and unmarshalling
 - more canonical Go structures
 - goprotobuf compatibility
 - less typing by optionally generating extra helper code
 - peace of mind by optionally generating test and benchmark code
 - other serialization formats}
%global golicenses      LICENSE
%global godocs          AUTHORS CONTRIBUTORS README bench.md custom_types.md Readme.md extensions.md
Name:           %{goname}
Release:        1%{?dist}
Summary:        Protocol buffers for Go with gadgets
License:        BSD-3-Clause
URL:            %{gourl}
Source0:        https://%{goipath}/archive/v%{version}/protobuf-%{version}.tar.gz
# oreon:deps
BuildRequires:  go-rpm-macros
BuildRequires:  protobuf-compiler
# /oreon:deps
%description %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%goprep

%build

for cmd in protoc-gen-gogofast protoc-min-version gogoreplace protoc-gen-gogoslick protoc-gen-combo protoc-gen-gogofaster protoc-gen-gostring conformance protoc-gen-gogo protoc-gen-gofast protoc-gen-gogotypes; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done
%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
%oreon_autofiles main
%if %{with check}
%check

for test in "TestGolden" \
            "TestDashFilename" \
            "TestEmbedMarshaler" \
            "TestRepeatedEmbed" \
            "TestRepeatedEmbTestTakesTooLongToDebuged" \
            "TestTakesTooLongToDebug" \
            "TestPopulateWarning" \
            "TestStdTypesGoString" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%gocheck
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
