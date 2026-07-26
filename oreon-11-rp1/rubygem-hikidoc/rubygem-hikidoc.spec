%global source0_hash 83938aee65028a73220764617dc95ab0e3e4daf0d774577825f64fb4e0f1c1dd

# Generated from hikidoc-0.0.6.gem by gem2rpm -*- rpm-spec -*-
%global	gem_name	hikidoc

Name:		rubygem-%{gem_name}
Version:	0.1.1
Release:	2%{?dist}

Summary:	Text-to-HTML conversion tool for web writers
License:	BSD-3-Clause
URL:		https://github.com/hiki/hikidoc
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	rubygem(test-unit)
Requires:	ruby(release)
Requires:	ruby(rubygems)
BuildArch:	noarch

%description
'HikiDoc' is a text-to-HTML conversion tool for web writers. 
HikiDoc allows you to write using an easy-to-read, easy-to-write plain 
text format, then convert it to structurally valid HTML (or XHTML).

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Cleanup
rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.github/ \
	.gitignore \
	.travis.yml \
	Gemfile \
	Rakefile \
	%{gem_name}.gemspec \
	test/
popd

%check
pushd .%{gem_instdir}

for f in test/*_test.rb
do
	ruby -Ilib:test:. $f
done
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/COPYING
%doc	%{gem_instdir}/[N-Z]*

%{_bindir}/hikidoc
%{gem_instdir}/bin

%{gem_libdir}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}/

%changelog
%autochangelog
