%global source0_hash 1b80cefcddd86eb423ed5a233a92c4d610b7c8e448f96c2850ae1ab35bee2975

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q repoquery --latest-limit 1 --whatprovides '" .. dep .. "' 2>/dev/null")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    local i = 1
    while i <= #out do
      local b = string.byte(out, i)
      if b ~= 32 and b ~= 9 and b ~= 10 and b ~= 13 then return false end
      i = i + 1
    end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.sub(s, 1, 3) == "%%if" and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.sub(s, 1, 3) == "%%if" then
          depth = depth + 1
        elseif string.sub(s, 1, 6) == "%%endif" then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.sub(s, 1, 5) == "%%else" then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.sub(dep, 1, 1) ~= "%%" and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond bootstrap 0

Name:           maven-resolver2
Epoch:          1
Version:        2.0.23
Release:        %autorelease
Summary:        Apache Maven Artifact Resolver library
License:        Apache-2.0
URL:            https://maven.apache.org/resolver/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/maven/resolver/maven-resolver-%{version}-source-release.zip

Patch:          0001-Remove-use-of-deprecated-SHA-1-and-MD5-algorithms.patch
Patch:          0002-Make-I-O-errors-during-test-cleanup-non-fatal.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-model-builder:4.0.0-rc-4)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider:4.0.0-rc-4)
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils:4.0.2)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:jcl-over-slf4j:2.0.17)
BuildRequires:  mvn(org.slf4j:slf4j-api:2.0.17)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:2.0.5-5

%description
Apache Maven Artifact Resolver is a library for working with artifact
repositories and dependency resolution. Maven Artifact Resolver deals with the
specification of local repository, remote repository, developer workspaces,
artifact transports and artifact resolution.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n maven-resolver-%{version}

# Skip tests that equire internet connection
#rm maven-resolver-supplier/src/test/java/org/eclipse/aether/supplier/RepositorySystemSupplierTest.java
#rm maven-resolver-transport-http/src/test/java/org/eclipse/aether/transport/http/{HttpServer,HttpTransporterTest}.java
%pom_remove_dep :jetty-bom

#%pom_remove_plugin -r :bnd-maven-plugin
#%pom_remove_plugin -r org.codehaus.mojo:animal-sniffer-maven-plugin
#%pom_remove_plugin -r :japicmp-maven-plugin

%pom_disable_module maven-resolver-demos
%pom_disable_module maven-resolver-named-locks-hazelcast
%pom_disable_module maven-resolver-named-locks-redisson
#%pom_disable_module maven-resolver-transport-classpath
#%mvn_package :maven-resolver-test-util __noinstall
%pom_disable_module maven-resolver-test-http
%pom_disable_module maven-resolver-transport-jetty
%pom_disable_module maven-resolver-transport-minio
%pom_disable_module maven-resolver-generator-sigstore
%pom_disable_module maven-resolver-generator-gnupg
%pom_disable_module maven-resolver-tools
%pom_disable_module maven-resolver-supplier-mvn3

%pom_remove_plugin :bnd-maven-plugin
%pom_remove_plugin :maven-jar-plugin

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :japicmp-maven-plugin

%mvn_compat_version : 2.0.23 2.0.9

%build
%mvn_build -j -f -j -- -Dmaven4Version=4.0.0-rc-4

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
%autochangelog
