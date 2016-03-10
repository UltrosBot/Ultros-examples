-- An example plugin for you to refer to when you're creating your own ones
-- You could also name this file "init.lua" if you wanted.

local plugin = ...  -- Get supplied plugin table from loader

function plugin.setup()
    --[[ Called when the plugin is loaded. Performs initial setup. ]]--

    -- Register the command in our system
    plugin.commands.register_command(
        "example",  -- The name of the command
        plugin.example_command,  -- The command's function
        plugin,  -- This plugin
        nil,  -- Required permission for command, eg "example.example"
        {"example2"},  -- Aliases for this command
        true  -- Whether this command should be available to all
    )
end

function plugin.example_command(protocol, caller, source, command, raw_args, args)
    --[[ Command handler for the example command ]]--

    if args == nil then
        -- This means that parsing failed for some reason, which will be
        -- invalid input for most plugins

        source.respond("Invalid args given!")
        return
    end

    -- Send to the channel
    source.respond("Hello, world! You ran the " .. command .. " command!")

    -- Send to the user that ran the command
    caller.respond("Raw arguments: " .. raw_args)
    caller.respond("Parsed arguments: " .. tostring(args))  -- This is a userdata value, so we have to cast it

    -- Send directly through the protocol
    protocol.send_msg(source, "Message through the protocol!")
end

-- Return the final plugin table to the loader
-- This table will be used as the plugin object
return plugin
