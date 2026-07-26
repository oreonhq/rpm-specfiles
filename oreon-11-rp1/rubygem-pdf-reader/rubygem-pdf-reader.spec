%global source0_hash 26a27981377a856ccbcaddc5c3001eab7b887066c388351499b0a1e07b53b4b3

%global gem_name pdf-reader

Name: rubygem-%{gem_name}
Version: 2.4.2
Release: 11%{?dist}
Summary: A library for accessing the content of PDF files
License: MIT
URL: https://github.com/yob/pdf-reader
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone --no-checkout https://github.com/yob/pdf-reader.git
# cd pdf-reader && git archive -v -o pdf-reader-2.4.2-spec.txz v2.4.2 spec/
Source1: pdf-reader-%{version}-spec.txz
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.3
BuildRequires: rubygem(Ascii85)
BuildRequires: rubygem(afm)
BuildRequires: rubygem(hashery)
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(ruby-rc4)
BuildRequires: rubygem(ttfunk)
BuildArch: noarch

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

%check
pushd .%{gem_instdir}
ln -s %{_builddir}/spec .

sed -i '/require.*bundler/ s/^/#/' spec/spec_helper.rb
sed -i '/Bundler.setup/ s/^/#/' spec/spec_helper.rb

rspec -r spec_helper spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/pdf_*
%license %{gem_instdir}/MIT-LICENSE
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/TODO
%doc %{gem_instdir}/CHANGELOG
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples

%changelog
%autochangelog
