%global source0_hash 9577affdf227d7b410f126f1f5a651086e34f749e3fc2fe6129d61a5b63b32ca

# Generated from pdf-inspector-1.0.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name pdf-inspector

Name: rubygem-%{gem_name}
Version: 1.3.0
Release: 18%{?dist}
Summary: A tool for analyzing PDF output
# Automatically converted from old format: GPLv2 or GPLv3 or Ruby - review is highly recommended.
License: GPL-2.0-only OR GPL-3.0-only OR Ruby
URL: https://github.com/prawnpdf/pdf-inspector
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/prawnpdf/pdf-inspector.git && cd pdf-inspector
# git checkout v1.3.0 && tar czvf pdf-inspector-1.3.0-spec.tgz spec/
Source1: pdf-inspector-%{version}-spec.tgz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(pdf-reader)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
This library provides a number of PDF::Reader[0] based tools for use in
testing PDF output.  Presently, the primary purpose of this tool is to
support the tests found in Prawn[1], a pure Ruby PDF generation library.
However, it may be useful to others, so we have made it available as
a gem in its own right.
[0] https://github.com/yob/pdf-reader
[1] https://github.com/sandal/prawn

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c -T -b 1
%gem_install -n %{SOURCE0}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec spec

# Don't use require_relative, it does not handle the symbolic link very well.
sed -i "/require_relative/ s|_relative '../lib/| '|" spec/spec_helper.rb

rspec spec
popd

%files
%dir %{gem_instdir}
%license %{gem_instdir}/COPYING
%license %{gem_instdir}/GPLv2
%license %{gem_instdir}/GPLv3
%license %{gem_instdir}/LICENSE
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.md
%doc %{gem_instdir}/README.md

%changelog
%autochangelog
