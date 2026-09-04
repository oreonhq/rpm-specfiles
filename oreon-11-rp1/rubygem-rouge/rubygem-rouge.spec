%global source0_hash b77c632842ab7f5147940212f0345808cccfbce864fd5b631d7d12a35ac85452
%global source1_hash 41e05c2ca61d0a523edfd9b556553de7011c172715e498e4985316bfbcafe395

%global gem_name rouge

Name:           rubygem-%{gem_name}
Version:        5.1.0
Release:        1%{?dist}
Summary:        Pure-ruby colorizer based on pygments
# From LICENSE file
# SPDX confirmed
License:        MIT AND BSD-2-Clause

URL:            http://rouge.jneen.net/
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        https://github.com/rouge-ruby/rouge/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}-test-missing-files.tar.gz
# SOURCE1 is created by $ bash %%SOURCE2 %%version
Source2:        rouge-create-missing-test-files.sh
Source10:       spec_helper_assert.rb
Source11:       bundler.rb
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  help2man
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rake)

BuildArch:      noarch

%description
Rouge aims to a be a simple, easy-to-extend drop-in replacement for pygments.


%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description    doc
Documentation for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

cp -a %{gem_name}-%{version}/spec .
mkdir FAKE
cp -a %{SOURCE11} FAKE/
cp -pa %{SOURCE10} spec/

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Generate man page from "rougify --help" output
export GEM_PATH="%{buildroot}%{gem_dir}:%{gem_dir}"

mkdir -p %{buildroot}%{_mandir}/man1
help2man -N -s1 -o %{buildroot}%{_mandir}/man1/rougify.1 \
    %{buildroot}%{_bindir}/rougify

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
    Gemfile \
    %{gem_name}.gemspec \
    %{nil}
popd

%check
find spec -name \*_spec.rb -print0 | \
	sort --zero-terminated |  \
	xargs --null ruby -Ilib:FAKE \
	-r./spec/spec_helper \
	-r./spec/spec_helper_assert \
	-r rake/rake_test_loader  \
	%{nil}

%files
%dir %{gem_instdir}

%license %{gem_instdir}/LICENSE

%{gem_libdir}
%exclude %{gem_libdir}/%{gem_name}/demos

%{_bindir}/rougify
%{gem_instdir}/bin
%{_mandir}/man1/rougify.1*

%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_libdir}/%{gem_name}/demos

%changelog
* Fri Sep 04 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.1.0-1
- Update to 5.1.0

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.7.0-2
- Import
