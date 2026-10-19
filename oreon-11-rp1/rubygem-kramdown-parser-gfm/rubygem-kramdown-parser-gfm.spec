%global source0_hash fb39745516427d2988543bf01fc4cf0ab1149476382393e0e9c48592f6581729
%global gem_name kramdown-parser-gfm
Name:           rubygem-%{gem_name}
Summary:        Kramdown parser for GitHub-flavored markdown
Version:        1.1.0
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/kramdown/parser-gfm
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:        https://github.com/kramdown/parser-gfm/commit/ad48572.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(kramdown)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rouge)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
kramdown-parser-gfm provides a kramdown parser for the GFM dialect of
Markdown.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch: noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
mv test/testcases/codeblock_fenced.text test/testcases/codeblock_fenced.disabled
ruby -I'lib' -e 'Dir.glob "./test/**test_*.rb", &method(:require)'
mv test/testcases/codeblock_fenced.disabled test/testcases/codeblock_fenced.text
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-kramdown-parser-gfm-doc -f %{oreon_filedir}/rubygem-kramdown-parser-gfm-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.0-17
- Prepare for Oreon 11 (RP1)
