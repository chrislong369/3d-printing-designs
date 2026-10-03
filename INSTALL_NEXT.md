# Recommended Next Installation Plan

Give Codex this instruction from the LongWorks-3D workspace:

1. Verify the existing LongWorks project context and local software.
2. Install the `heyixuan2/bambu-studio-ai` agent skill using its documented skill installer.
3. Run its dependency doctor and report PASS/WARN/FAIL. Do not configure paid AI providers yet.
4. Clone and inspect `mackson/blender-mcp`. Before installing the Blender add-on or changing Codex MCP configuration, show me exactly what will be changed and wait for approval.
5. Verify FreeCAD. If installed, clone and prepare `neka-nat/freecad-mcp`, again showing configuration changes before applying them.
6. Verify CadQuery availability in an isolated Python environment.
7. Do NOT install Meshy MCP because my current Meshy account does not have paid API access.
8. Verify Bambu Studio location and version.
9. Run a read-only end-to-end diagnostic and produce a table:
   - component
   - installed?
   - version
   - path
   - integration status
   - action needed
10. Do not create a model yet.

After approval, configure Blender MCP and run a test where Codex creates one small object in Blender, captures a viewport/render preview, exports it, validates it, and opens the output in Bambu Studio.
