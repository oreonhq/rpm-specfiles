%global source1_hash 7ad17c861f4237ae5cfce4c0315f282a5d64fecb43f6bdd6890ee0053bc03afe
%global source0_hash 26a27981377a856ccbcaddc5c3001eab7b887066c388351499b0a1e07b53b4b3
%global gem_name pdf-reader
Name: rubygem-%{gem_name}
Version: 2.4.2
Release:        1%{?dist}
Summary:        A library for accessing the content of PDF files
License: MIT
URL: https://github.com/yob/pdf-reader
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: https://github.com/yob/pdf-reader/archive/refs/tags/v2.4.2.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(Ascii85)
BuildRequires:  rubygem(afm)
BuildRequires:  rubygem(hashery)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(ruby-rc4)
BuildRequires:  rubygem(ttfunk)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The PDF::Reader library implements a PDF parser conforming as much as possible
to the PDF specification from Adobe.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n  %{gem_name}-%{version} -b 1
find %{_builddir} -mindepth 2 -type d \( -name test -o -name tests -o -name spec -o -name specs \) -exec cp -a {} %{_builddir}/ \;

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
chmod a+x %{buildroot}%{gem_instdir}/examples/*.rb
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ln -s %{_builddir}/spec .
sed -i '/require.*bundler/ s/^/#/' spec/spec_helper.rb
sed -i '/Bundler.setup/ s/^/#/' spec/spec_helper.rb
rspec -r spec_helper spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-pdf-reader-doc -f %{oreon_filedir}/rubygem-pdf-reader-doc.list

%changelog

%autochangelog
